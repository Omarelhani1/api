from flask import Flask, render_template,abort,request
import json
import os
import requests
app = Flask(__name__)
url_base="https://covid-api.mmediagroup.fr/v1/"
url_base1="https://restcountries.eu/rest/v2/name/"
url_base2="https://restcountries.eu/rest/v2/alpha/"
@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/buscar_pais',methods=["GET","POST"])
def buscar_pais():
    nombre_pais=request.form.get("nombre")
    if request.method == "GET":
        return render_template("buscar_pais.html", nombre_pais=nombre_pais)
    else:
        parametros={"country":nombre_pais}
        r=requests.get(url_base+'/cases',params=parametros)
        doc=r.json()
        confirmados=doc.get("All").get("confirmed")
        recuperados=doc.get("All").get("recovered")
        muertos=doc.get("All").get("deaths")
        poblacion=doc.get("All").get("population")
        return render_template("buscar_pais.html",nombre_pais=nombre_pais,confirmados=confirmados,recuperados=recuperados,muertos=muertos,poblacion=poblacion)

@app.route('/buscar_continente',methods=["GET","POST"])
def buscar_continente():
	return render_template("buscar_continente.html")

@app.route('/buscar_iniciales',methods=["GET","POST"])
def buscar_iniciales():
	return render_template("buscar_iniciales.html")

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)
