from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Gestante(db.Model):
    __tablename__ = 'gestantes'  # nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)  # CPF da gestante
    nome = db.Column(db.String(100), nullable=False)  # Nome da gestante
    data_nascimento = db.Column(db.Date, nullable=False)  # Data de nascimento
    idade = db.Column(db.Integer)  # Idade
    nome_mae = db.Column(db.String(100), nullable=False)  # Nome da mãe
    data_prevista_parto = db.Column(db.Date, nullable=False)  # Data prevista para o parto
    ultima_menstruacao = db.Column(db.Date, nullable=False)  # Data da última menstruação
    endereco = db.Column(db.String(200), nullable=False)  # Endereço
    cep = db.Column(db.String(8), nullable=False)  # CEP
    cidade = db.Column(db.String(100), nullable=False)  # Cidade
    estado = db.Column(db.String(100), nullable=False)  # Estado
    telefone = db.Column(db.String(20), nullable=False)  # Telefone

    def to_dict(self):
        return {
            "id": self.id,
            "cpf": self.cpf,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime('%Y-%m-%d') if self.data_nascimento else None,
            "idade": self.idade,
            "nome_mae": self.nome_mae,
            "data_prevista_parto": self.data_prevista_parto.strftime('%Y-%m-%d') if self.data_prevista_parto else None,
            "ultima_menstruacao": self.ultima_menstruacao.strftime('%Y-%m-%d') if self.ultima_menstruacao else None,
            "endereco": self.endereco,
            "cep": self.cep,
            "cidade": self.cidade,
            "estado": self.estado,
            "telefone": self.telefone
        }
