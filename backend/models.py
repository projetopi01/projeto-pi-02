from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from sqlalchemy import Enum
import enum

db = SQLAlchemy()

# Enum para os status do exame
class StatusEnum(str, enum.Enum):
    pendente = "pendente"
    proximo = "próximo"
    concluido = "concluído"

class Gestante(db.Model):
    __tablename__ = 'gestantes'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nome_mae = db.Column(db.String(100), nullable=False)
    data_prevista_parto = db.Column(db.Date, nullable=False)
    ultima_menstruacao = db.Column(db.Date, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    exames = db.relationship('Exame', back_populates='gestante', cascade='all, delete-orphan')

    @property
    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - (
            (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

    def to_dict(self):
        return {
            "id": self.id,
            "cpf": self.cpf,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime('%Y-%m-%d'),
            "idade": self.idade,
            "nome_mae": self.nome_mae,
            "data_prevista_parto": self.data_prevista_parto.strftime('%Y-%m-%d'),
            "ultima_menstruacao": self.ultima_menstruacao.strftime('%Y-%m-%d'),
            "endereco": self.endereco,
            "cep": self.cep,
            "cidade": self.cidade,
            "estado": self.estado,
            "telefone": self.telefone
        }


class Exame(db.Model):
    __tablename__ = 'exames'
    id = db.Column(db.Integer, primary_key=True)
    gestante_id = db.Column(db.Integer, db.ForeignKey('gestantes.id'), nullable=False)
    nome_exame = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date)
    status = db.Column(Enum(StatusEnum), default=StatusEnum.pendente)  # Usando Enum para status
    cor_status = db.Column(db.String(7))  # Ex: '#FF0000'

    gestante = db.relationship('Gestante', back_populates='exames')

    def to_dict(self):
        return {
            "id": self.id,
            "gestante_id": self.gestante_id,
            "nome_exame": self.nome_exame,
            "data": self.data.strftime('%Y-%m-%d') if self.data else None,
            "status": self.status.value,  # Garantindo que o status seja uma string
            "cor_status": self.cor_status
        }
