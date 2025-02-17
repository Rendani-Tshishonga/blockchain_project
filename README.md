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

