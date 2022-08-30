from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Vamos por FLASK para Backend con Python'

    #Siempre correr set FLASK_APP=main.py en la terminal para evitar el erro de varialbes