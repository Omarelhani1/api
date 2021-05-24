from flask import Flask, render_template,abort,request
import json
import os
app = Flask(__name__)
@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)