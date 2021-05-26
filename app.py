from flask import Flask, render_template,abort,request
import json
import os
app = Flask(__name__)
@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/buscar_pais',methods=["GET","POST"])
def buscar_pais():
	return render_template("buscar_pais.html")

@app.route('/buscar_continente',methods=["GET","POST"])
def buscar_continente():
	return render_template("buscar_continente.html")

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)