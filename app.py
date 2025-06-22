from flask import Flask, request, jsonify
from flask import render_template
import configuracion as c
from user_agents import parse
from datetime import datetime

import os

app=Flask(__name__)
app.config['SECRET_KEY']=c.Opcion().get_keyPrivada()
application=app


@app.route("/",methods=['GET','POST'])
def index():
    user_agente=request.headers.get('User-Agent')
    parse_agente = parse(user_agente)
    if parse_agente.is_mobile:
        if "Android" in user_agente:
            dispositivo = "Android"
        elif "iPhone" in user_agente:
            dispositivo = "iPhone"
        else:
            dispositivo = "Otro móvil"
    else:
        dispositivo = "WEB"
    print(user_agente)
    return render_template('index.html',device=dispositivo, mensaje=determinar_momento_del_dia())


@app.route("/inicio")
def inicio():
    return render_template('estructura/inicio.html', mensaje=determinar_momento_del_dia())
#-----------------------------------------------------------------------------------------------MIERCOLES
@app.route('/miercoles')
def miercoles():
    return render_template('1_miercoles/1_miercoles.html')


#-----------------------------------------------------------------------------------------------JUEVES
@app.route('/jueves')
def jueves():
    return render_template('2_jueves/1_jueves.html')


#-----------------------------------------------------------------------------------------------viernes
@app.route('/viernes')
def viernes():
    return render_template('3_viernes/1_viernes.html')

#-----------------------------------------------------------------------------------------------sabado
@app.route('/sabado')
def sabado():
    return render_template('4_sabado/1_sabado.html')

#-----------------------------------------------------------------------------------------------domingo
@app.route('/domingo')
def domingo():
    return render_template('5_domingo/1_domingo.html')





#-----------------------------------------------------------------------------------------------ERRORES
@app.errorhandler(404)
def page_not_found(error):
    return render_template('estructura/404.html')

@app.route('/service-worker.js')
def service_worker():
    return app.send_static_file('js/service-worker.js')


def determinar_momento_del_dia():
    hora_actual = datetime.now().hour  # Obtiene la hora actual

    if 6 <= hora_actual < 8:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>Hola buenos días✌️</h3>"
    elif 8 <= hora_actual < 13:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>Buena jornada 👩‍🏭🪚</h3>"
    elif 13<= hora_actual <14:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>🍢A comeer!! 🍕</h3>"
    elif 14 <= hora_actual < 18:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>☀️🫡Buena tarde </h3>"
    elif hora_actual==19:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>⛪Vamos a misa ✝️</h3>"
    elif 20 <= hora_actual < 21:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>vamos a cenar🌃</h3>"
    elif 21 <= hora_actual < 24:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>Buenas actividades nocturnas<br>🌉🌓🌙</h3>"
    else:
        return "<h3 class='text-center' style='padding-left: 5%; padding-right: 5%;'>🤫🥷shhh deben estar durmiendo🛌🏕️</h3>" 

if __name__ == '__main__':
    app.run(debug=True,port=5001)
