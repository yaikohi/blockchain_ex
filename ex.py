import json
import time

from block import Block
from blockchain import Blockchain

new_ex_coin = Blockchain()
# new_ex_coin.add_block((1, "10/02/2021", { "amount": 4 }))
# new_ex_coin.add_block((2, "12/02/2021", { "amount": 10 }))

print(new_ex_coin)
print(time.ctime(new_ex_coin.chain[0].timestamp))
print(type(new_ex_coin.create_genesis_block))