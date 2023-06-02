from flask import Flask, render_template
import os

# Inicializar la aplicacion
app = Flask(__name__, template_folder="templates")
app._static_folder = os.path.abspath("templates/static/")


@app.route("/", methods=["GET", "POST"])  # Ruta principal
def home():
    return render_template("layouts/home.html")


# main del programa
if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicacion
