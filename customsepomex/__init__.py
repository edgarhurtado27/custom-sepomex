from flask import Flask, jsonify, abort, request, Response
from . import mongoclient

# Instanciamos el servidor
app = Flask(__name__)

@app.route('/custom/ping')
def ping():
    return jsonify({ 'mensaje': 'App Online' })

@app.route('/custom/sepomex/<string:zipCode>', methods=['POST', 'GET'])
def customSepomexHandler(zipCode):
    if not zipCode.isnumeric() : abort(400)

    if request.method == 'POST':
        tmpObj = {}
        tmpObj['zipCode'] = zipCode
        mongoclient.CustomMongoClient.insertOne('zipCodes', tmpObj)
        return jsonify({ 'code': 200, 'message': 'Object inserted'})

    query = {}
    query['zipCode'] = zipCode
    result = mongoclient.CustomMongoClient.findOne('zipCodes', query)

    if result is None : abort(404)

    return jsonify(result), 200, {'ContentType':'text/html'}

