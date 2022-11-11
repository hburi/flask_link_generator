#!/usr/bin/env python3



from flask import Flask, render_template, request
from funciones import link_maker

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("formulario.html")


@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = link_maker(request.form.get("nombre"))
    #edad = request.form.get("edad")
    #edad = suma_eldoble(request.form.get("edad"))
    return render_template("mostrar.html", nombre=nombre)



def suma_eldoble(entrada):
    salida = entrada + ' ' + str(int(entrada) * 2)
    return(salida)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
