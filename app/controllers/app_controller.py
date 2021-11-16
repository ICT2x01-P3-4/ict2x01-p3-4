from flask import render_template
def index():
    return render_template("index.html")
def userhome():
    return render_template("userhome.html")