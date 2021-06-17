import time
from block import Block

class Blockchain:
    """The blockchain class containing all the blocks.
    
    Attributes:
        chain: an array containing blocks starting from the Genesisblock at array index 0.
    
    
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