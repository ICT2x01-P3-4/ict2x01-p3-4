from flask import render_template
def index():
    return render_template("index.html")
def freestyle():
    return render_template("freestyle_mode.html")