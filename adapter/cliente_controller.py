from flask import jsonify
from domain.entities.cliente_entity import ClienteEntity

def getClienteById(clientId):
    cliente = ClienteEntity()
    cliente.id = clientId
    cliente.nome = "João da Silva Sauro"
    return jsonify(cliente)