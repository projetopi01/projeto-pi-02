from flask import Blueprint, jsonify
from models import db, Gestante, Exame

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/gestantes', methods=['GET'])
def get_gestantes():
    # Consultar as gestantes
    gestantes = Gestante.query.all()

    # Verificar se há gestantes
    if not gestantes:
        return jsonify({"message": "Nenhuma gestante encontrada"}), 404

    # Preparar os dados para resposta
    gestantes_lista = [
        {
            "id": gestante.id,
            "cpf": gestante.cpf,
            "nome": gestante.nome,
            "data_nascimento": gestante.data_nascimento.strftime('%Y-%m-%d') if gestante.data_nascimento else None,
            "idade": gestante.idade,
            "nome_mae": gestante.nome_mae,
            "data_prevista_parto": gestante.data_prevista_parto.strftime('%Y-%m-%d') if gestante.data_prevista_parto else None,
            "ultima_menstruacao": gestante.ultima_menstruacao.strftime('%Y-%m-%d') if gestante.ultima_menstruacao else None,
            "endereco": gestante.endereco,
            "cep": gestante.cep,
            "cidade": gestante.cidade,
            "estado": gestante.estado,
            "telefone": gestante.telefone,
            "exames": [
                {
                    "tipo_exame": exame.tipo_exame,
                    "data_exame": exame.data_exame.strftime('%Y-%m-%d') if exame.data_exame else None,
                    "resultado": exame.resultado,
                    "status": exame.status,  # Aqui, pegamos o status (pendente, próximo, concluído)
                    "cor_status": get_status_color(exame.status)  # Aqui obtemos a cor do status
                }
                for exame in gestante.exames
            ]
        } for gestante in gestantes
    ]

    return jsonify(gestantes_lista), 200


def get_status_color(status):
    # Defina a cor de acordo com o status do exame
    if status == 'pendente':
        return 'yellow'
    elif status == 'concluído':
        return 'green'
    elif status == 'próximo':
        return 'blue'
    return 'gray'  # cor padrão caso o status não seja reconhecido
