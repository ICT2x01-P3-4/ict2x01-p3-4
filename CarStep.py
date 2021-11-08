from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)