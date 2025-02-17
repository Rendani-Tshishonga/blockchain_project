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
    """ We run a proof of work algorithm to get the next proof """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    """ Reward for finding the proof """
    """ The sender is "0" to signify that this node has mined a new coin """
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    """ Forge the new block by adding it to the chain """
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transaction': block['transaction'],
        'proof': block['proof'],
        'previous_hash' block['previous_hash'],
    }

    return jsonify(response), 200

""" Create a route to create a new transaction """
@app.route("/transactions/new", methods=['POST'])
def new_transaction():
    values = request.get_json()

    """ Check that required fields are in the POST data """
    required = ["sender", "recipient", "amount"]
    if not all(k in values for k in required):
        return 'Missing values', 400

    """ Create a new transaction """
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to block {index}')
    return jsonify(response), 201

""" Create a route to return a blockchain """
@app.route("/chain", methods=['GET'])
def chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route("/nodes/register", methods=['GET'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route("/nodes/resolve", methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
