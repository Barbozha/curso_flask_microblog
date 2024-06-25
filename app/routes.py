from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    nome = 'Jorge Paulo'
    dados = {'profissao':'Desenvolvedor', 'email':'barbozha@gmail.com'}
    return render_template('index.html', name=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
