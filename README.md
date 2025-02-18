# Blockchain Project

## What is Blockchain?

Blockchain is an immutable, sequential chain of records called block. They contain transactions, files, or any data you like.
The important aspect about a blockchain is that all these block are chained together. We will dive into some of the concepts I have learned builing this blockchain. I would like to acknowledge Daniel van Flymen a Blockchain Engineer in sharing his experience on how to build one from scratch using the Python.

## What does a block look like?

```
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
	{
	    'sender': "8527147fe1f5426f9dd",
	    'recipient': "a77f5cdfa2934df3",
	    'amount': 5,
	}
    ]
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26c3b2ac"
}
```
## Blockchain Implementation

The Blockchain implementation will be centered around four main methods:
	
	1. Creating new transactions.
	2. Creating new blocks.
	3. Proof Of Work.
	4. Consesus.

## Creating new transactions

The new_transactions() method will create a new transaction to the list and it returns the index of the block.

## Creating a new block

When our block is instantiated we'll need to seed it with a genesis block which is a block with no predecessors. We'll need to add a "proof" to the genesis block which is the result of mining or the proof of work.

## Proof of work

A proof of work is how new block are created in the chain or mined on the blockchain. The goal of the proof of work is to discover the number which solves the problem and mines a new coin each time we are able to solve this problem. The problem should be difficult to solve but easy to verify.

The problem is solved by assuming that the hash of some integer multipied by another integer must end with 0.

```
from hashlib import sha256

x = 5
y = 0 # We dont know what y should be yet (proof)

while sha256(f'{x * y}'.encode()).hexdigest()[-1] != 0:
	y += 1
print(f'The solution is y = {y}')
```
Bitcoins proof of work algorithm is called hash cash. This is the algorithm that miners race to mine in order to create a new block. The difficulty is determined by the number of characters searched for in a string. The miners are then rewarded for their solution by recieving a coin in a transaction.

## Consensus

The whole point of Blockchain is that they should be decentralized. This brings about a conflict as multiple chains may arise from different nodes so we need to ensure that the nodes reflect the same chain and not different chains. This is consensus, as we will implement a consensus algorithm to track the different nodes so we can find the authoritative chain or in other words the longest chain  so we have nodes in different netwoks which reflect the same chain.
