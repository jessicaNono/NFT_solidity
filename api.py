from flask import Flask
from flask import request, jsonify,render_template
from web3 import Web3, middleware
import json
from web3.exceptions import ContractLogicError
from web3.gas_strategies.time_based import *
from web3.middleware import geth_poa_middleware
from flask_cors import CORS, cross_origin
import random
import binascii

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/filparty": {"origins": "http://127.0.0.1:4444"}})



w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
compile_contract_path = 'build/contracts/LTL.json'
with open(compile_contract_path) as file:
    contract_json = json.load(file)
    contract_abi = contract_json

connected = w3.isConnected()
status = False
if connected:
    geth = w3.geth
    eth = w3.eth
    contract =  w3.eth.contract(address=w3.toChecksumAddress('0x96F7784AC5B983390D4de23c426B03B7c1B8cf0E'), abi=contract_abi['abi'])
    status = True 

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@app.route('/flask/api/v1/epitech/', methods=['GET'])
def epitech():
    desc =  "Photo test"
    image = "http://127.0.0.1:4444/static/logo-epitech.png"
    name = "Epitech"

    return jsonify(name= name, description = desc, image=image)

@app.route('/flask/api/v1/mintnft/', methods=['GET'])
def mintnft():
    with open("~/.ethereum/keystore/UTC--2018-06-10T05-43-22.134895238Z--6b26E13f086194309fC2adFd5519188DA3B74b22") as keyfile:
        encrypted_key = keyfile.read()
        private_key = w3.eth.account.decrypt(encrypted_key,'password')
        print(binascii.b2a_hex(private_key))

    uri = request.args.get('uri')
    acc = request.args.get('account')
    acc = w3.toChecksumAddress(acc)
    nonce = w3.eth.get_transaction_count(acc) 
   
    statusmint = False
    if status == True:
        try:
            result = contract.functions.mintNFT(acc, uri).buildTransaction({'from':acc, 'nonce':nonce})
            signed_txn = w3.eth.account.sign_transaction(result, private_key=private_key)
            send = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

            tx_receipt = w3.eth.wait_for_transaction_receipt(send)  
            statusmint = True
        except ValueError:
            statusmint = False
    
    return  jsonify(status= statusmint)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4444)
