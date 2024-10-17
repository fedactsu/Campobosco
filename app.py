from flask import Flask, request, jsonify, make_response, redirect, send_file,url_for
from flask import render_template
import configuracion as c
import mysql.connector
from datetime import timedelta
import datetime as dt
import locale
import zipfile
import bcrypt
import os

app=Flask(__name__)
app.config['SECRET_KEY']=c.Opcion().get_keyPrivada()
application=app

#print(c.Opcion().get_anioActualTotal())


@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

#-----------------------------------------------------------------------------------------------ERRORES
@app.errorhandler(404)
def page_not_found(error):
    return render_template('view/errores/404.html')



if __name__ == '__main__':
    app.run(debug=True,port=5001)
