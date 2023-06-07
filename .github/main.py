from flask import Flask, render_template, redirect, url_for

# starten app: gewoon runnen met play, door regel onder if name_main
# stoppen: rechter muisknop stop code run.
# dit commando werkt ook:
# python -m flask --app main run (main is bestandsnaam)

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route('/home')
def home():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
