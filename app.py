import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from categorizer import categorize
from skill_extractor import extract_skills
from relationship import build_relationships

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store uploaded documents
documents = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["document"]

        if file:

            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            category = categorize(filename)

            # Save document details
            skills = extract_skills(filename)

            documents.append({
                "name": filename,
                "category": category,
                "skills": skills
            })

            # Open Dashboard
            return redirect(url_for("dashboard"))

    return render_template("upload.html")



@app.route("/search", methods=["GET", "POST"])
def search():

    results = []

    if request.method == "POST":

        query = request.form["query"].lower()

        for doc in documents:

            if (
                query in doc["name"].lower()
                or query in doc["category"].lower()
                or any(query in skill.lower() for skill in doc["skills"])
            ):
                results.append(doc)

    return render_template("search.html", results=results)
@app.route("/timeline")
def timeline():

    return render_template("timeline.html", files=documents)


@app.route("/relationships")
def relationships():

    data = build_relationships(documents)

    return render_template(
        "relationships.html",
        data=data
    )

@app.route("/dashboard")
def dashboard():

    stats = {
        "total": len(documents),
        "certificates": len([d for d in documents if d["category"] == "Certification"]),
        "projects": len([d for d in documents if d["category"] == "Project"]),
        "internships": len([d for d in documents if d["category"] == "Internship"])
    }

    return render_template(
        "dashboard.html",
        files=documents,
        stats=stats
    )
if __name__ == "__main__":
    app.run(debug=True)