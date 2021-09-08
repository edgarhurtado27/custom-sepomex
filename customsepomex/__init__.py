from flask import Flask, jsonify, abort
from . import mongoclient


config = {
    "DEBUG": True,
    "JSON_AS_ASCII": False
}

# Instanciamos el servidor
app = Flask(__name__)
app.config.from_mapping(config)


@app.route('/custom/ping')
def ping():
    return jsonify({ 'mensaje': 'App Online' })

@app.route('/custom/sepomex/<string:zipCode>', methods=['GET'])
def customSepomexHandler(zipCode):
    if not zipCode.isnumeric() : abort(400)

    query = {}
    query['codigoPostal'] = zipCode
    result = mongoclient.CustomMongoClient.findOne('zipCodes', query)

    if result is None : abort(404)
    print(result)

    return jsonify(result), 200, {'ContentType':'text/html'}

