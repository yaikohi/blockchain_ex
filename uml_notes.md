# classes

## block
### attributes
**hash** : int
**previous_hash** : int
**transactions** : str
### methods
createBlock(inout transactions: str, Block.hash: int): Block
getHash(out): Self.hash: int

## transaction
### attributes
**balance**: int
**fee** : int
**address_receiver** : str
**address_sender** : str
### methods
getTransactionBalance
getAddressReceiver( out ): Self.address_receiver: str
getAddressSender( out ): Self.address_sender: str

# Objects
## genesis_block 
[src](https://genesisblockhk.com/what-is-the-genesis-block/)
object

### attributes
**hash**: 0
**previous_hash**: 0
**transactions**: ["0", "0",]
### methods
createBlock(inout transactions: str, Block.hash: int): Block
createHash(out self.previous_hash, self.transactions): hash str
getHash(out): 0 (Self.hash)

