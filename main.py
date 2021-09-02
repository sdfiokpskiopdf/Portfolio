from flask import Flask, render_template, url_for
import json
import os

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/projects")
def projects():
    with open("projects.json") as json_file:
        projects = json.load(json_file)
    
    print(projects) 
    return render_template("projects.html", projects=projects)


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Dynamically named static files
# Solves problems related to browser cache
# /static/css/style.css?q=1280549780
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values["q"] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4000)
