from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, João! Esse é o seu primeiro site! Parabéns, cabeção!"

app.route("/sobre")
def sobre():
  return "João Gabriel Leite é jornalista e Redator".

app.route("/contato")
def contato():
  return "não tem, eu não quero ser contatado por ninguém."
