from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("food.html")

@app.route("/home")
def home1():
    return render_template("food.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/receipe")
def receipe():
    return render_template("Receipe.html")


@app.route("/contact")
def contact():
    return render_template("Contact.html")






if __name__ == "__main__":
    app.run(debug=True, port=8000)
