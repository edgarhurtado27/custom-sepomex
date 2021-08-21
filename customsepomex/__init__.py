from flask import Flask, jsonify, abort

# Instanciamos el servidor
app = Flask(__name__)

@app.route('/custom/ping')
def ping():
    return jsonify({ 'mensaje': 'App Online' })


@app.route('/custom/sepomex/<string:zipCode>')
def getZipCode(zipCode):
    if not zipCode.isnumeric() : abort(400)
    return jsonify({ 'zipCode': zipCode })

