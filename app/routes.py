from app import app
from flask import render_template, request, flash, redirect

@app.route('/')
@app.route('/index', defaults={'nome':'Usuário', 'profissao':'Profissão','contato':'contato'})
@app.route('/index/<nome>/<profissao>/<contato>')
def index(nome, profissao, contato):
    #nome = 'Jorge Paulo'
    #dados = {'profissao':'Desenvovedor','contato':'barbozha@gmail.com'}
    dados = {'profissao':profissao, 'contato':contato}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == 'admin123':
        return 'usuario: {} e senha:{}'.format(usuario, senha)
    else:
        flash('Dados inválidos')
        flash('Login ou senha enválidos')
        return redirect('/login')
