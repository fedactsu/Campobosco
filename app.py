from flask import Flask, request, jsonify
from flask import render_template
import configuracion as c
from user_agents import parse
from datetime import datetime
import textos_primera_tanda as tpt
import os

app=Flask(__name__)
app.config['SECRET_KEY']=c.Opcion().get_keyPrivada()
application=app

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

def obtenerdias():
    return [
        ['domingo','/domingo','2️⃣9️⃣'],
        ['lunes','/lunes','3️⃣0️⃣'],
        ['martes','/martes','0️⃣1️⃣'],
        ['miércoles','/miercoles','0️⃣2️⃣'],
        ['jueves','/jueves', '0️⃣3️⃣'],
        ['viernes','/viernes','0️⃣4️⃣'],
        ['sábado','/sabado','0️⃣5️⃣']
    ]

def obteneroracion():
    return ['laudes','vísperas','completas']

@app.route("/inicio")
def inicio():
    return render_template('estructura/inicio.html',dia=obtenerdias())
@app.route("/base")
def base():
    return render_template('estructura/base.html')
#-----------------------------------------------------------------------------------------------DOMINGO
@app.route('/domingo')
def domingo():
    dia="Domingo 29"
    onomastico = "San Pablo y San Pedro apóstoles"
    return render_template('1_DOMINGO/1_DOMINGO.html',domingo=obteneroracion(),dia=dia,onomastico=onomastico)
#-----------------------------------------------------------------------------------------------LUNES
@app.route('/lunes')
def lunes():
    return render_template('2_LUNES/2_LUNES.html')
#-----------------------------------------------------------------------------------------------MARTES
@app.route('/martes')
def martes():
    return render_template('3_MARTES/3_MARTES.html')
#-----------------------------------------------------------------------------------------------MIÉRCOLES
@app.route('/miercoles')
def miercoles():
    return render_template('4_MIERCOLES/4_MIERCOLES.html')
#-----------------------------------------------------------------------------------------------JUEVES
@app.route('/jueves')
def jueves():
    return render_template('5_JUEVES/5_JUEVES.html')
#-----------------------------------------------------------------------------------------------VIERNES
@app.route('/viernes')
def viernes():
    return render_template('6_VIERNES/6_VIERNES.html')
#-----------------------------------------------------------------------------------------------SABADO
@app.route('/sabado')
def sabado():
    return render_template('7_SABADO/7_SABADO.html')
#-----------------------------------------------------------------------------------------------ERRORES
@app.errorhandler(404)
def page_not_found(error):
    return render_template('estructura/404.html')
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('estructura/500.html')



if __name__ == '__main__':
    app.run(debug=True,port=5001)
