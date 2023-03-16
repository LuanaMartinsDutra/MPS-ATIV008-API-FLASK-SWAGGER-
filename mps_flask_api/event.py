from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

EVENT = {
    "1000": {
        "evento_nome": "Consulta medica",
        "evento_id": "1000",
        "evento_descricao": "Consulta com cardiologista",
        "evento_data": "2023-03-30",
        "user_id": "1000",
        "timestamp": get_timestamp(),
    },
    "2000": {
        "evento_nome": "Dentista",
        "evento_id": "2000",
        "evento_descricao": "Manuntecao do aparelho",
        "evento_data": "2023-03-22",
        "user_id": "2000",
        "timestamp": get_timestamp(),
    },
    "3000": {
        "evento_nome": "Apresentacao de Metodologia",
        "evento_id": "3000",
        "evento_descricao": "Apresentacao do trabalho final",
        "evento_data": "2023-03-23",
        "user_id": "3000",
        "timestamp": get_timestamp(),
    }

}

def read_all():
    return list(EVENT.values())


def create(evento):
    evento_id = evento.get("evento_id", "")
    evento_nome = evento.get("evento_nome", "")
    evento_data = evento.get("evento_data", "")
    evento_desc = evento.get("evento_desc", "")
    user_id = evento.get("user_id", "")

    if evento_id and evento_id not in EVENT:
        EVENT[evento_id] = {
            "evento_id": evento_id,
            "evento_nome": evento_nome,
            "evento_data": evento_data,
            "evebto_desc": evento_desc,
            "user_id": user_id,
            "timestamp": get_timestamp(),
        }
        return EVENT[evento_id], 201
    else:
        abort(
            406,
            f"User with last name {evento_nome} already exists",
        )


def read_one(evento_id):
    if evento_id in EVENT:
        return EVENT[evento_id]
    else:
        abort(
            404, f"Person with ID {evento_id} not found"
        )


def update(evento_id, evento):
    if evento_id in EVENT:
        EVENT[evento_id]["evento_nome"] = evento.get("evento_name", EVENT[evento_id]["evento_nome"])
        EVENT[evento_id]["evento_data"] = evento.get("evento_data", EVENT[evento_id]["evento_data"])
        EVENT[evento_id]["evento_desc"] = evento.get("evento_desc", EVENT[evento_id]["evento_desc"])
        EVENT[evento_id]["timestamp"] = get_timestamp()
        return EVENT[evento_id]
    else:
        abort(
            404,
            f"Person with ID {evento_id} not found"
        )


def delete(evento_id):
    if evento_id in EVENT:
        del EVENT[evento_id]
        return make_response(
            f"{evento_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {evento_id} not found"
        )