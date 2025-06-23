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

def obtenercoso():
    return [
        ["Domingo 29 de junio", "San Pablo y San Pedro apóstoles", "1_DOMINGO/1_DOMINGO.html"],
        ["Lunes 30 de junio", "Decimotercera semana del Tiempo Ordinario", "2_LUNES/2_LUNES.html"],
        ["Martes 01 de julio", "Decimotercera semana del Tiempo Ordinario", "3_MARTES/3_MARTES.html"],
        ["Miércoles 02 de julio", "Decimotercera semana del Tiempo Ordinario", "4_MIERCOLES/4_MIERCOLES.html"],
        ["Jueves 03 de julio", "Decimotercera semana del Tiempo Ordinario - Santo Tomás apóstol", "5_JUEVES/5_JUEVES.html"],
        ["Viernes 04 de julio", "Decimotercera semana del Tiempo Ordinario", "6_VIERNES/6_VIERNES.html"],
        ["Sábado 05 de julio", "Decimotercera semana del Tiempo Ordinario", "7_SABADO/7_SABADO.html"]
    ]

@app.route("/inicio")
def inicio():
    return render_template('estructura/inicio.html',dia=obtenerdias())
@app.route("/base")
def base():
    return render_template('estructura/base.html')
#-----------------------------------------------------------------------------------------------DOMINGO
@app.route('/domingo')
def domingo():
    lec = tpt.PrimeraTanda().lecturadomingo()
    return render_template(obtenercoso()[0][2],domingo=obteneroracion(),dia=obtenercoso()[0][0],onomastico=obtenercoso()[0][1],lec=lec)
#-----------------------------------------------------------------------------------------------LUNES
@app.route('/lunes')
def lunes():
    return render_template(obtenercoso()[1][2],domingo=obteneroracion(),dia=obtenercoso()[1][0],onomastico=obtenercoso()[1][1])
#-----------------------------------------------------------------------------------------------MARTES
@app.route('/martes')
def martes():
    return render_template(obtenercoso()[2][2],domingo=obteneroracion(),dia=obtenercoso()[2][0],onomastico=obtenercoso()[2][1])
#-----------------------------------------------------------------------------------------------MIÉRCOLES
@app.route('/miercoles')
def miercoles():
    return render_template(obtenercoso()[3][2],domingo=obteneroracion(),dia=obtenercoso()[3][0],onomastico=obtenercoso()[3][1])
#-----------------------------------------------------------------------------------------------JUEVES
@app.route('/jueves')
def jueves():
    return render_template(obtenercoso()[4][2],domingo=obteneroracion(),dia=obtenercoso()[4][0],onomastico=obtenercoso()[4][1])
#-----------------------------------------------------------------------------------------------VIERNES
@app.route('/viernes')
def viernes():
    return render_template(obtenercoso()[5][2],domingo=obteneroracion(),dia=obtenercoso()[5][0],onomastico=obtenercoso()[5][1])
#-----------------------------------------------------------------------------------------------SABADO
@app.route('/sabado')
def sabado():
    return render_template(obtenercoso()[6][2],domingo=obteneroracion(),dia=obtenercoso()[6][0],onomastico=obtenercoso()[6][1])
#-----------------------------------------------------------------------------------------------ERRORES
@app.errorhandler(404)
def page_not_found(error):
    return render_template('estructura/404.html')
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('estructura/500.html')



if __name__ == '__main__':
    app.run(debug=True,port=5001)
