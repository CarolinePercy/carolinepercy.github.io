from flask import Flask, request, render_template, session
from flask_session import Session
import datetime
import random
import requests
from collections import Counter


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# What to be stored in session:
# the generated word, player's start & end time, players word input
# IP address, operating system, browser


@app.get("/")  # register the / URL with the Flask web server
def home_page():
    return render_template("mainPage.html")

@app.get("/contact")  # register the / URL with the Flask web server
def contact_page():
    return render_template("contact.html")

@app.get("/about")  # register the / URL with the Flask web server
def about_page():
    return render_template("about.html")

@app.get("/projects")  # register the / URL with the Flask web server
def project_page():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)
