from flask import Flask, render_template, request, redirect, session, flash, url_for

class Filamento:
    def __init__(self, cor, fornecedor, descricao, qtd):
        self.cor = cor
        self.fornecedor = fornecedor
        self.descricao = descricao      
        self.qtd = qtd 

filamento1 = Filamento('Vermelho','Volt','Vermelho','1000')
filamento2 = Filamento('Azul piscina','National','Azul tiffany','500')
filamento3 = Filamento('Branco','National','Branco gelo','300')
lista = [filamento1 ,filamento2 ,filamento3]       
 
class Usuario:
    def __init__ (self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
       
usuario1 = Usuario('Luiza', 'Lu', '1234')
usuario2 = Usuario('Leone', 'Leo', '1235')
usuario3 = Usuario('Laura', 'Laurita', '1236')

usuarios = { usuario1.nickname :usuario1, 
                usuario2.nickname :usuario2,
                usuario3.nickname :usuario3 }

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('lista.html',titulo='Filamentos Empresa 3D Silveira', filamentos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima = url_for('novo')))
    return render_template('cadastro.html',titulo='Cadastro de Filamento')

@app.route('/criar', methods=['POST',])
def criar():
    cor = request.form['cor']
    fornecedor = request.form['fornecedor']
    descricao = request.form['descricao']
    qtd = request.form['quatidade']
    filamento4 = Filamento(cor,fornecedor,descricao,qtd)
    lista.append(filamento4)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios [request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso ')
            return redirect(url_for('novo'))
            
    else:
        flash('Usuario não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))
    
app.run(debug=True, port=5002)