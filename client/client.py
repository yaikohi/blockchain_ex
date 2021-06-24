import binascii
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_OAEP


class Client:    
    """Applies signatures to transactions made on the blockchain. 

    Attributes:
        _private_key: A unique (hidden) key of the client used to generate a 
            signature for each blockchain transaction the client sends out. 
            Used in combination with the _public_key.
        _public_key: A unique public key of the client used to generate a 
            signature for each blockchain transaction the client sends out. 
            Used in combination with the _private_key.
        _signer: A unique signing key of the client.
            Used for signing a transaction on the blockchain.

    Example:
        Instantiating the class by Object = Client() and 
        then calling Object.identity returns the public key.
    """
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_OAEP.new(self._private_key)

    @property
    def public_key(self) -> str:
        """Returns the public key.

        Returns:
            public_key[str]: a hexadecimal public key. 
        """
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


class User:
    """A user with a unique id, a name, and a balance containing currency.
    
    -- TODO: add extra info here --
    
    Attributes:
        id[int]: A unique key id that specifies the user.
        name[str]: The name of the user.
        balance[float]: a value describing the currency available to the user.
    """ 
    def __init__(self, 
                 id: int, 
                 name: str, 
                 balance: float):
        self.id = id
        self.name = name
        self.balance = balance
    
    @property
    def balance(self):
        return self.balance
    
    @balance.setter
    def receive_value(self, n_currency_received: float):
        """Updates the balance after receiving n currency"""
        return self._set_balance(n_currency_received)
    
    @balance.setter
    def send_value(self, n_currency_sent: float):
        """Updates the balance after sending n currency"""
        return self._set_balance(n_currency_sent)
    
    def _set_balance(self, value: float):
        """Indirect setter to calculate the new balance"""
        return (self.balance + value)