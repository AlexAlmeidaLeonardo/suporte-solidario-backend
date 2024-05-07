from flask import jsonify
from datetime import date
from domain.entities.usuario_entity import UsuarioEntity

def getUsuarioById(usuarioId):
    usuario = UsuarioEntity()
    usuario.id = usuarioId
    usuario.login = "joao"
    usuario.criacao = date.today()
    usuario.alteracao = usuario.criacao
    usuario.celular = "11993153668"
    usuario.email = "aal2005@gmail.com"
    usuario.tipo_de_usuario = 1
    return jsonify(usuario)