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
        r1=requests.get(url_base1+nombre_pais)
        if r1.status_code==200:
            parametros={"country":nombre_pais}
            r=requests.get(url_base+'/cases',params=parametros)
            doc=r.json()
            confirmados=doc.get("All").get("confirmed")
            recuperados=doc.get("All").get("recovered")
            muertos=doc.get("All").get("deaths")
            poblacion=doc.get("All").get("population")
            return render_template("buscar_pais.html",nombre_pais=nombre_pais,confirmados=confirmados,recuperados=recuperados,muertos=muertos,poblacion=poblacion)
        else:
            return abort(404)

@app.route('/buscar_ciudad',methods=["GET","POST"])
def buscar_ciudad():
    nombre_pais=request.form.get("nombre")
    nombre_ciudad=request.form.get("nombre1")
    if request.method == "GET":
        return render_template("buscar_ciudad.html",nombre_ciudad=nombre_ciudad, nombre_pais=nombre_pais)
    else:
        parametros={"country":nombre_pais}
        r=requests.get(url_base+'/cases',params=parametros)
        doc=r.json()
        confirmados=doc.get(nombre_ciudad).get("confirmed")
        recuperados=doc.get(nombre_ciudad).get("recovered")
        muertos=doc.get(nombre_ciudad).get("deaths")
        return render_template("buscar_ciudad.html",nombre_ciudad=nombre_ciudad,nombre_pais=nombre_pais,confirmados=confirmados,recuperados=recuperados,muertos=muertos)

@app.route('/buscar_iniciales',methods=["GET","POST"])
def buscar_iniciales():
    inicial=request.form.get("nombre")
    if request.method == "GET":
        return render_template("buscar_iniciales.html", inicial=inicial)
    else:
        r1=requests.get(url_base2+inicial)
        if r1.status_code==200:
            parametros={"ab":inicial}
            r=requests.get(url_base+'/cases',params=parametros)
            doc=r.json()
            confirmados=doc.get("All").get("confirmed")
            recuperados=doc.get("All").get("recovered")
            muertos=doc.get("All").get("deaths")
            poblacion=doc.get("All").get("population")
            return render_template("buscar_iniciales.html",inicial=inicial,confirmados=confirmados,recuperados=recuperados,muertos=muertos,poblacion=poblacion)
        else:
            return abort(404)
port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=True)
