from typing import List
from hashlib import sha256

class ExampleCoinBlock:
    def __init__(self, previous_block_hash, transaction: str):
        self.previous_block_hash: str = previous_block_hash
        self.transaction: str = transaction
        self.block_data: List = [transaction.replace('\n', ''), previous_block_hash]
        self.block_hash: str = sha256(self.block_data[0].encode(encoding='UTF-8') + self.block_data[1].encode(encoding="UTF-8")).hexdigest()


class Transaction:
    def __init__(self, sender, receiver, balance_sent, fee):
        self.sender: str = sender
        self.receiver: str = receiver
        self.balance_sent: float = balance_sent
        self.fee: float = fee

    def get_transaction_data(self):
        return f'{self.sender} sent <{self.balance_sent}> ExC to {self.receiver}. The fee is: <{self.fee}> ExC. Total amount transferred: <{self.balance_sent - self.fee}> ExC.'


class User:
    def __init__(self, first_name, second_name):
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.address: str = sha256(self.first_name.encode(encoding='UTF-8') + self.second_name.encode(encoding='UTF-8')).hexdigest()
        self.balance: int = 0

    def update_balance(self, value):
        self.balance += value
    
    

genesis_block = ExampleCoinBlock("0", "0")

u1 = User("Mike", "Casey")
u2 = User("Paul", "Coser")
t1 = Transaction(u1.first_name, u2.first_name, 5.4, 0.2)
block_t1 = ExampleCoinBlock(genesis_block.block_hash, t1.get_transaction_data())


print(f"Sender name: {t1.sender}")
print(f"Receiver name: {t1.receiver}")
print(f"Balance sent: {t1.balance_sent}")
print(f"Transaction fee: {t1.fee}\n")

print(f"Previous block hash: {block_t1.previous_block_hash}")
print(f"Transaction data: {block_t1.transaction}")
print(f"Block data: {block_t1.block_data}")
print(f"Block hash: {block_t1.block_hash}\n")