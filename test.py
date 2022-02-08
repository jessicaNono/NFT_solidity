from flask import Flask
from flask import request, jsonify,render_template
from web3 import Web3, middleware
import json
from web3.exceptions import ContractLogicError
from web3.gas_strategies.time_based import *
from web3.middleware import geth_poa_middleware
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/filparty": {"origins": "http://127.0.0.1:4444"}})

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

@app.route('/flask/api/v1/epitech/', methods=['GET'])
def epitech():
    desc =  "Epitech logo"
    image = "http://127.0.0.1:4444/static/logo-epitech.png"
    name = "Epitech"

    return jsonify(name= name, description = desc, image=image)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4444)
