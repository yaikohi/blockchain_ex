import time
from typing import List
import time
import json
from hashlib import sha256


class Blockchain:
    """The blockchain class containing all the blocks.

    Attributes:
        chain: an array containing blocks with Genesisblock index 0.
    """

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate a genesis block and append it to
        the chain.
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        """
        A quick pythonic way to retrieve the most recent block in the chain.
        """
        return self.chain[-1]


class Block:
    def __init__(self):
        """ Constructor for the `Block` class.

        Args:
            index: Unique ID of the block.
            transactions: List of transactions.
            timestamp: Time of generation of the block.
            previous_hash: Hash of the previous block in the chain which this block is part of.

        Returns:
            An instance of the `Block` class. A block object.
        """
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""
 
    def compute_hash(self):
        """
        Returns the hash of the block instance.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True) # The string equivalent also considers the previous_hash field now
        return sha256(block_string.encode()).hexdigest()
