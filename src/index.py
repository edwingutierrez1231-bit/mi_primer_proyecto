import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # Esto toma el puerto dinámico que te asigne Render en internet.
    # Si estás en tu computadora (local), usará el puerto 5000 por defecto.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
