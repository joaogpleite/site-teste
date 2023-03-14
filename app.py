from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">Página Inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return menu + "Olá, João! Esse é o seu primeiro site! Parabéns!"

app.route("/sobre")
def sobre():
  return menu + "João Gabriel Leite é jornalista e Redator".

app.route("/contato")
def contato():
  return menu + "não tem, eu não quero ser contatado por ninguém."
