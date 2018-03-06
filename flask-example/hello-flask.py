from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return "fook you, welcumback home..."

@app.route("/index")
def index():
    return "index.hhhhhhh"

@app.route("/main-page")
def main_page():
    return "this is the fookin main page"

@app.route("/user/<username>")
def profile(username):passt

with app.test_request_context():
    print(url_for('index'))
    print(url_for('main_page'))

if __name__ == "__main__":
    app.run()
