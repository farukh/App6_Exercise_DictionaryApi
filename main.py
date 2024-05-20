from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def dictionary(word):
    return word.capitalize()

app.run(debug=True,port=5001) #if port is occupied, we can run like this\


