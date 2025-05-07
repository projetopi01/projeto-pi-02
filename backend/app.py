from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'erlandsonsilvadonascimento')

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    idade = db.Column(db.Integer)
    nome_mae = db.Column(db.String(100), nullable=False)
    data_prevista_parto = db.Column(db.Date, nullable=False)
    ultima_menstruacao = db.Column(db.Date, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d'),
            'idade': self.idade,
            'nome_mae': self.nome_mae,
            'data_prevista_parto': self.data_prevista_parto.strftime('%Y-%m-%d'),
            'ultima_menstruacao': self.ultima_menstruacao.strftime('%Y-%m-%d'),
            'endereco': self.endereco,
            'cep': self.cep,
            'cidade': self.cidade,
            'estado': self.estado,
            'telefone': self.telefone
        }

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

# Decorador para proteger as rotas que precisam de login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # Verifica se o usuário está autenticado
            flash('Você precisa estar logado para acessar essa página.')
            return redirect(url_for('login'))  # Redireciona para a página de login
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('login_page.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = os.getenv('APP_USERNAME', 'usuario')
        password = os.getenv('APP_PASSWORD', '123456')
        entered_username = request.form.get('username')
        entered_password = request.form.get('password')
        if entered_username == username and entered_password == password:
            session['user_id'] = entered_username  # Armazena o usuário na sessão
            return redirect(url_for('cadastro_gestante'))
        else:
            error_message = "Usuário ou senha incorretos."
            return render_template('login_page.html', error=error_message)
    else:
        return render_template('login_page.html')

@app.route('/cadastro_gestante', methods=['GET'])
@login_required  # Protege a rota de cadastro de gestantes
def cadastro_gestante():
    return render_template('cadastro_gestante.html')

@app.route('/submit', methods=['POST'])
@login_required  # Protege a rota de submit, se necessário
def submit():
    cpf = request.form.get('cpf')
    nome = request.form.get('nome')
    data_nascimento = datetime.strptime(request.form.get('data_nascimento'), '%Y-%m-%d')
    idade = (datetime.now() - data_nascimento).days // 365
    nome_mae = request.form.get('nome_mae')
    data_prevista_parto = datetime.strptime(request.form.get('data_prevista_parto'), '%Y-%m-%d')
    ultima_menstruacao = datetime.strptime(request.form.get('ultima_menstruacao'), '%Y-%m-%d')
    endereco = request.form.get('endereco')
    cep = request.form.get('cep')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    telefone = request.form.get('telefone')

    novo_usuario = Usuario(
        cpf=cpf, nome=nome, data_nascimento=data_nascimento,
        idade=idade, nome_mae=nome_mae, data_prevista_parto=data_prevista_parto,
        ultima_menstruacao=ultima_menstruacao, endereco=endereco, cep=cep,
        cidade=cidade, estado=estado, telefone=telefone
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return redirect(url_for('success'))  # Redireciona para a página de sucesso

@app.route('/success', methods=['GET'])
def success():
    return render_template('success_page.html')  # Renderiza a página de sucesso

@app.route('/api/gestante/<cpf>', methods=['GET'])
@login_required  # Protege a rota da API, se necessário
def get_gestante(cpf):
    usuario = Usuario.query.filter_by(cpf=cpf).first()
    if usuario:
        return jsonify(usuario.to_dict()), 200
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove o usuário da sessão
    return redirect(url_for('login'))  # Redireciona para a página de login

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa a porta fornecida pelo Render
    app.run(host="0.0.0.0", port=port)  # Faz o app escutar em todas as interfaces
