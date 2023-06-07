from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import pymongo
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_BASEDATOS = "ServiEntrega"  # nombre de la base de datos
bdd = pymongo.MongoClient(MONGO_URI)
baseDatos = bdd[MONGO_BASEDATOS]


# Inicializar la aplicación
app = Flask(__name__, template_folder='templates')              #indica la carpte de los templates
app._static_folder = os.path.abspath("templates/static/")                       #Carpeta static de los templates


@app.route("/", methods=["GET", "POST"])  # Ruta principal
def home():
    return render_template("layouts/home.html")

#--CLIENTES--
@app.route("/clientes", methods=["GET", "POST"])  
def clientes():
    clientes_collection = baseDatos["Clientes"]
    resultados = clientes_collection.find()


    return render_template("layouts/clientes.html", clientes_datos=resultados)

@app.route("/RegistroCliente", methods=["GET", "POST"])  
def RegistroCliente():
    if(request.method == "POST"):
        ultimo_documento = baseDatos.Clientes.find_one({}, sort=[('_id', -1)])
        print(ultimo_documento)

        if ultimo_documento is not None:
            ultimo_id = int(ultimo_documento['_id'])
            nuevo_id = ultimo_id + 1
        else:
            nuevo_id = 1
        nuevo_id_str = str(nuevo_id).zfill(3)

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['correo']
        cedula = request.form['cedula']
        cliente = {
            "_id": nuevo_id_str,
            "Nombre": nombre,
            "Apellido": apellido,
            "Direccion": direccion,
            "NumeroTelefono": telefono,
            "CorreoElectronico": correo,
            "Cedula": cedula,
        }
        baseDatos.Clientes.insert_one(cliente)
        return redirect(url_for('clientes'))

    return render_template("layouts/clientes.html")

@app.route("/EliminarCliente", methods=["GET", "POST"])  
def EliminarCliente():
    if(request.method == "POST"):
        id = request.form['_id']
        baseDatos.Clientes.delete_one({"_id": id})

        return redirect(url_for('clientes'))

    return render_template("layouts/clientes.html")

@app.route("/UpdateCliente", methods=["GET", "POST"])  
def UpdateCliente():
    clientes_collection = baseDatos["Clientes"]
    resultados = clientes_collection.find()

    if request.method == "POST":
        id_cliente = request.form["_idCliente"]
        nombre_cliente = baseDatos.Clientes.find({"_id": id_cliente})

        return render_template("layouts/clientes.html", clientes_datos=resultados, DatoCliente=nombre_cliente)

    return render_template("layouts/clientes.html", clientes_datos=resultados)




#--REPARTIDORES--
@app.route("/repartidores", methods=["GET", "POST"])  
def repartidores():
    repartidores_collection = baseDatos["Repartidores"]
    resultados = repartidores_collection.find()

    if request.method == "POST":
        id_repartidor = request.form["_idRepartidor"]
        nombre_repartidor = baseDatos.Repartidores.find({"_id": id_repartidor})

        return render_template("layouts/repartidores.html", repartidores_datos=resultados, DatoRepartidor=nombre_repartidor)

    return render_template("layouts/repartidores.html", repartidores_datos=resultados)

@app.route("/RegistroRepartidor", methods=["GET", "POST"])  
def RegistroRepartidor():
    if(request.method == "POST"):
        ultimo_documento = baseDatos.Repartidores.find_one({}, sort=[('_id', -1)])
        print(ultimo_documento)

        if ultimo_documento is not None:
            ultimo_id = int(ultimo_documento['_id'])
            nuevo_id = ultimo_id + 1
        else:
            nuevo_id = 1

        nuevo_id_str = str(nuevo_id).zfill(3)

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        cedula = request.form['cedula']
        vehiculo = {
            "Tipo": request.form['vehiculo'],
            "Placa": request.form['placa'],
            "Modelo": request.form['modelo']
        }
        repartidor = {
            "_id": nuevo_id_str,
            "Nombre": nombre,
            "Apellido": apellido,
            "NumeroTelefono": telefono,
            "Vehiculo": vehiculo,
            "Cedula" : cedula
        }
        baseDatos.Repartidores.insert_one(repartidor)

        return redirect(url_for('repartidores'))

    return render_template("layouts/repartidores.html")

@app.route("/EliminarRepartidor", methods=["GET", "POST"])  
def EliminarRepartidor():
    if(request.method == "POST"):
        id = request.form['_id']
        baseDatos.Repartidores.delete_one({"_id": id})

        return redirect(url_for('repartidores'))

    return render_template("layouts/repartidores.html")

@app.route("/UpdateRepartidores", methods=["GET", "POST"])  
def UpdateRepartidores():
    repartidores_collection = baseDatos["Repartidores"]
    resultados = repartidores_collection.find()


    return render_template("layouts/repartidores.html", repartidores_datos=resultados)


# main del programa
if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicación
