""" Load Libraries """

import haslib
import json
from time import time

""" A program to create a blockchain """

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        
        """ Create a genesis block """
        self.new_block(previous_hash=1, proof=100)

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
        - Find a number p' such that hash(pp') contains 4 leading zeros, where p
        - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: does hash(last_proof, proof) contain 4 leading zeros?
        :param last_proof: <int> previous proof.
        :param proof: <int> the current proof.
        :return: <bool> True if correct, false if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def new_block(self, proof, previous_hash=None):
        """ 
        Creates a new block and adds it to the chain
        :param proof: <int> the proof given by the proof of work algorithm
        :param previous_hash: (optional) <str> hash of previous Block
        :return: <dict> New Block

        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        """Reset the current list of transactions"""
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """ 
        Creates a new transaction to get into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction

        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block
        :param block: <dict> Block
        :return: <str>

        """
        """ 
        We need to convert the dictionary to a JSON formatted string and ensure that the 
        dictionary is ordered or we'll have inconsistent hashes.

        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """ Returns the last block in the chain """
        return self.chain[-1]
