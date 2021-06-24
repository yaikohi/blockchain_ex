import time
import json
from hashlib import sha256

# Global variable
LAST_BLOCK_HASH = ""


class Blockchain:
    """The blockchain class containing all the blocks.

    Attributes:
        chain (list): an array containing blocks with a Genesisblock at index 0.
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
    """ A block on the blockchain.

    Attributes:
        verified_transactions (`list`[:obj: client.transaction.Transaction]): List of verified transactions, 
            a transaction gets verified after receiving a signature of a client.
        previous_block_hash (str): Hash of the previous block on the blockchain. 
        Nonce (str): A unique value for the instantiated block.
    """

    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    def compute_hash(self):
        """Computes the hash of the block instance.

        Returns: 
            (str): Hashed value.
        """
        block_string = json.dumps(
            self.__dict__, sort_keys=True)  # The string equivalent also considers the previous_hash field now
        return sha256(block_string.encode()).hexdigest()
