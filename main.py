from bd import Carros
from flask import Flask, jsonify, make_response, request # type: ignore

#instanciar o modo flask na nossa varial
app = Flask('carros')       

#primeiro metodo - primeiro end point - GET

@app.route('/carros', methods=['GET'])
#app rout é para defirnie que essa função é uma rota , para que o flask entenda que isso é uma função a ser excutada

def get_carros():
    return Carros

#primeiro metodo -  end point - GET / ID

@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get("id") == id:
            return jsonify(carro)

#segundo metodos - criar novos dados - POST
@app.route('/carros', methods=['POST'])
def criar_carro():
    carro = request.json
    Carros.append(carro)

    return make_response(
        jsonify(mensagem = 'Carro cadastrado com sucesso',
                carro = carro
                )#mensagem de carro cadastrado
    )

#terceiro metodo = editar daados - PUT
@app.route('/carros/<int:id>', methods=['PUT'])

def editar_carros(id):
    carroalterado = request.get_json()
    for indice,carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carroalterado)#alterando os valores com update
            return jsonify(Carros[indice])

#quarto metodo - deletar - DELETE

@app.route('/carros/<int:id>', methods=['DELETE'])

def excluir_carro(id):
    carrosexcluir = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem":"Carro excluido com sucesso"})

app.run(port=5000,host='localhost')