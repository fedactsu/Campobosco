from flask import Flask, request, jsonify, make_response, redirect, send_file,url_for
from flask import render_template
import configuracion as c
import mysql.connector
from datetime import timedelta
import datetime as dt
import locale
import zipfile
import os

app=Flask(__name__)
app.config['SECRET_KEY']=c.Opcion().get_keyPrivada()
application=app

#print(c.Opcion().get_anioActualTotal())


@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/inicio")
def inicio():
    return render_template('estructura/inicio.html')
#-----------------------------------------------------------------------------------------------MIERCOLES
@app.route('/miercoles')
def miercoles():
    return render_template('1_miercoles/1_miercoles.html')

@app.route('/miercoles/laudes')
def miercoles_laudes():
    return render_template('1_miercoles/2_mier_laudes.html')

@app.route('/miercoles/misa')
def miercoles_misa():
    return render_template('1_miercoles/3_mier_misa.html')


#-----------------------------------------------------------------------------------------------ERRORES
@app.errorhandler(404)
def page_not_found(error):
    return render_template('estructura/404.html')



if __name__ == '__main__':
    app.run(debug=True,port=5001)
