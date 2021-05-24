from app import app
from flask import render_template, request, jsonify, send_from_directory, abort, redirect
import json
import os
from module import get_xoso


with open("./data/data.json") as f:
	data = json.load(f)
	jobs = data["jobs"]
	posts = data["posts"]
	time = data["time"]


@app.route("/", methods = ["GET","POST"])
def index():
	if request.method == 'POST':
		numbers = request.form["check_number"]
		checked_result = get_xoso.solve(numbers.split(" ")) 
		return render_template("index.html", time = time, checked_result = checked_result, jobs = jobs, posts = posts)
	else:
		return render_template("index.html", time = time, jobs = jobs, posts = posts)
@app.route("/about")
def about():
	return render_template("about.html",)

if __name__ == '__main__':
	app.run(debug=True)