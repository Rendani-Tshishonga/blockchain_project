""" Import Libraries """

from blockchain import Blockchain
from flask import Flask, jsonify, request
from uuid import uuid4

""" Instantiate a Node """
app = Flask(__name__)

""" Generate a globally unique address for this node """
node_identifier = str(uuid4()).replace('-', '')

""" Instantiate the Blockchain """
blockchain = Blockchain()

""" Create a route to mine a new block """
@app.route("/mine", methods=['GET'])
def mine():
    return "We'll mine a new block"

""" Create a route to create a new transaction """
@app.route("/transactions/new", methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

""" Create a route to return a blockchain """
@app.route("/chain", methods=['GET'])
def chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
