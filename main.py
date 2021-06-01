import hashlib


class ExampleCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2 ExC to Mike"
t2 = "Mike sends 5.4 ExC to Paul"
t3 = "An sends 233 ExC to Bob"
t4 = "Michael sends 2.0 ExC to Ben"
t5 = "Louise sends 1 ExC to Lee"
t6 = "Kees sends 0.3 ExC to Mike"

initial_block = ExampleCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash, "\n")

second_block = ExampleCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data) 
print(second_block.block_hash, "\n")

third_block = ExampleCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash, "\n")