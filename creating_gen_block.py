from client.client import *
from client.transaction import *
from blockchain.blockchain import *

"""Example code for creating a genesis block and the first hashed value for the blockchain.
"""
# 1. Instantiate the genesis client.
GenesisClient = Client()

# 2. Instantiate the first transaction.
transaction_0 = Transaction(
    "Genesis",
    GenesisClient.public_key,
    500.0
)
# 3. Instantiate a block-object: `GenesisBlock`.
GenesisBlock = Block()

# 4. Set the `previous_block_hash` attribute of the GenesisBlock to None.
GenesisBlock.previous_block_hash = None

# 5. Set the `Nonce` attribute of the GenesisBlock to None.
GenesisBlock.Nonce = None

# 6. Append the first transaction to the `verified_transactions` attribute of the GenesisBlock.
GenesisBlock.verified_transactions.append(transaction_0)

# 7. Save the hashed value of the GenesisBlock.
digest = hash(GenesisBlock)

# 8. This hashed value is now equal to the `LAST_BLOCK_HASH` global variable of the blockchain.
LAST_BLOCK_HASH = digest
