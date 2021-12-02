#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
#@app.route("/start") # or user can land at "/start"
def start():
    return render_template("question.html") # look for templates/question.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location

@app.route("/answer", methods = ["POST"])
def askquestion():
    # POST from question.html template
    if request.form:
        team_name = request.form.get("team")
        if (team_name.lower() == "green bay" or team_name.lower() == "green bay packers" or team_name.lower() == "packers"): # if the answer is correct
            return redirect("correct")
        else: # Ask again
            return redirect("/")
    if request.json:
        data = request.json
        print(data)
        if data["team_name"] == "green bay":
            return redirect("correct")
        else: # Ask again
            return "That is INCORRECT"
   
@app.route("/correct")
def correct():
    return "You are correct!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

