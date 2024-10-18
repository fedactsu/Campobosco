from flask import Flask, request, jsonify, make_response, redirect, send_file
from flask import render_template
import configuracion as c

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


#-----------------------------------------------------------------------------------------------JUEVES
@app.route('/jueves')
def jueves():
    return render_template('2_jueves/1_jueves.html')

@app.route('/jueves/laudes')
def jueves_laudes():
    return render_template('2_jueves/2_jueves_laudes.html')

@app.route('/jueves/misa')
def jueves_misa():
    return render_template('2_jueves/3_jueves_misa.html')

#-----------------------------------------------------------------------------------------------viernes
@app.route('/viernes')
def viernes():
    return render_template('3_viernes/1_viernes.html')

@app.route('/viernes/laudes')
def viernes_laudes():
    return render_template('3_viernes/2_viernes_laudes.html')

@app.route('/viernes/misa')
def viernes_misa():
    return render_template('3_viernes/3_viernes_misa.html')

#-----------------------------------------------------------------------------------------------sabado
@app.route('/sabado')
def sabado():
    return render_template('4_sabado/1_sabado.html')

@app.route('/sabado/laudes')
def sabado_laudes():
    return render_template('4_sabado/2_sabado_laudes.html')

@app.route('/sabado/misa')
def sabado_misa():
    return render_template('4_sabado/3_sabado_misa.html')
#-----------------------------------------------------------------------------------------------domingo
@app.route('/domingo')
def domingo():
    return render_template('5_domingo/1_domingo.html')

@app.route('/domingo/laudes')
def domingo_laudes():
    return render_template('5_domingo/2_domingo_laudes.html')

@app.route('/domingo/misa')
def domingo_misa():
    return render_template('5_domingo/3_domingo_misa.html')

#-----------------------------------------------------------------------------------------------cancionero
@app.route('/cancionero')
def cancionero():
    return render_template('6_cancionero/6_cancionero_general.html')

#-----------------------------------------------------------------------------------------------ERRORES
@app.errorhandler(404)
def page_not_found(error):
    return render_template('estructura/404.html')

@app.route('/service-worker.js')
def service_worker():
    return app.send_static_file('js/service-worker.js')

if __name__ == '__main__':
    app.run(debug=True,port=5001)
