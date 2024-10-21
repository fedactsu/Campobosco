from flask import Flask, request
from flask import render_template
import configuracion as c
import cancionero as can
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

@app.route("/comoagregar")
def comoagregar():
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
    return render_template('estructura/agregaralinicio.html', device=dispositivo )

@app.route("/inicio")
def inicio():
    return render_template('estructura/inicio.html', mensaje=determinar_momento_del_dia())
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

@app.route('/miercoles/horario')
def miercoles_horario():
    return render_template('1_miercoles/4_mier_horario.html')

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

@app.route('/jueves/horario')
def jueves_horario():
    return render_template('2_jueves/4_jueves_horario.html')

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

@app.route('/viernes/horario')
def viernes_horario():
    return render_template('3_viernes/4_viernes_horario.html')

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

@app.route('/sabado/horario')
def sabado_horario():
    return render_template('4_sabado/4_sabado_horario.html')
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

@app.route('/domingo/horario')
def domingo_horario():
    return render_template('5_domingo/4_domingo_horario.html')
#-----------------------------------------------------------------------------------------------vocacional
@app.route('/vocacional')
def vocacional():
    return render_template('8_vocacional/8_vocacional.html')

#-----------------------------------------------------------------------------------------------mapa
@app.route('/mapalugar')
def mapa():
    return render_template('7_mapa/7_mapa1.html')

#-----------------------------------------------------------------------------------------------cancionero
@app.route('/cancionero')
def cancionero():
    cancionero = [[0,"👓Himno CAMPOBOSCO🎶"],
                  [1,"🙏Creemos en el Dios que ama a los jóvenes👦"],
                  [2,"🚶Don Bosco Amigo🤸‍♂️"],
                  [3,"🔊Haz cantar tu vida🎙️"],
                  [4,"Señor ten piedad🙏 (C. Fones)"],
                  [5,"Oh Señor, ten  piedad🎼"],
                  [6,"Kyrie eleison🎵"],
                  [7,"👦Gloria a Dios 🙏(C. Fones)"],
                  [8,"🙏Gloria a ti eterno amor💕"],
                  [9,"⚓Dios está aquí🎶"],
                  [10,"👩‍🦰Margaritas💐"],
                  [11,"🎤Aleluya, gloria  aleluya🎶"],
                  [12,"😁Aleluya vivo estás📍"],
                  [13,"😊En Ti Señor😉"],
                  [14,"📌Donde hay amor💞"],
                  [15,"🥖Tomad, Señor y recibid🍷"],
                  [16,"En tus manos🤚 hoy"],
                  [17,"Santo🎶🎵 (C. Fones)"],
                  [18,"Santo continental🌐"],
                  [19,"Cordero juvenil👧🧒"],
                  [20,"Cordero🐑 de Dios"],
                  [21,"👩‍🏫Don Bosco enséñanos👨‍🏫"],
                  [22,"👨‍👩‍👧‍👦Procura hacerte amar👩‍👦"],
                  [23,"Contigo  María👸"],
                  [24,"👸👩‍👦Auxiliadora de don Bosco"],
                  [25,"María es👸"],
                  [26,"María mírame👸🧒👧"],
                  ]
    return render_template('6_cancionero/6_cancionero_general.html',canciones=cancionero )

@app.route('/cancionero/<idcancion>', methods=['GET'])
def cancionparticular(idcancion):
    cancionero=[[can.cancionero().himnodonbosco],
                [can.cancionero().getCan1()],
                [can.cancionero().getCan2()],
                [can.cancionero().hazcantartuvida],
                [can.cancionero().senortenpiedad],
                [can.cancionero().ohsenortenpiedad],
                [can.cancionero().kyrieeleison],
                [can.cancionero().gloriaadiosfones],
                [can.cancionero().gloriatieternoamor],
                [can.cancionero().diosestaaqui],
                [can.cancionero().margaritas],
                [can.cancionero().aleluya1],
                [can.cancionero().aleluya2],
                [can.cancionero().entisenor],
                [can.cancionero().dondehayanmor],
                [can.cancionero().tomadyrecibir],
                [can.cancionero().entusmanoshoy],
                [can.cancionero().santofones],
                [can.cancionero().santocontinental],
                [can.cancionero().corderojuvenil],
                [can.cancionero().corderodios],
                [can.cancionero().donboscoensenanos],
                [can.cancionero().procurahacerteamar],
                [can.cancionero().contigomaria],
                [can.cancionero().auxiliadoradonbosco],
                [can.cancionero().mariaes],
                [can.cancionero().mariamirame],
                ]
    return render_template('6_cancionero/6_1_cancionero_especifico.html',letra=cancionero[int(idcancion)][0] )





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
