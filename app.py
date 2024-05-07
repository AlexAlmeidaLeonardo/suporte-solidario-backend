import sys
import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from adapter import cliente_controller, usuario_controller

# A linha que faz os arquivos poderem se referenciarem
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a secret key
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    login = request.json.get('login')
    password = request.json.get('password')

    # Verificamos se o usuário e senha existe no banco de dados
    if login == 'admin' and password == 'password':
        access_token = create_access_token(identity=login)
        return jsonify(access_token=access_token)
    return jsonify({"mensagem": "Usuário/senha inválido!"}), 401

@app.route('/usuario/<usuario_id>', methods=['GET'])
@jwt_required()
def get_usuario(usuario_id):
    return usuario_controller.getUsuarioById(usuario_id)

@app.route('/cliente/<client_id>', methods=['GET'])
@jwt_required()
def get_cliente(client_id):
    return cliente_controller.getClienteById(client_id)

if __name__ == '__main__':
    app.run(debug=True)