from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)
app.secret_key = "123Vivalalgerie"

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
