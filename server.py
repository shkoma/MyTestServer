from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route("/")
def main():
    print("Hello")

if __name__ == "__main__":
    app.run()