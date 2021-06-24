import datetime
import collections
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import binascii


class Transaction:
    """A transaction class.

    To instantiate a `transaction` object it requires: a senders' public key, 
    the receivers' public key, and a value that denotes the amount to be transferred.

    Args:
        sender: a senders' public key
        recipient: a recipients' public key
        value: a value
    """

    def __init__(self,
                 sender: str,
                 recipient: str,
                 value: float):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            public_key = "Genesis"
        else:
            public_key = self.sender.public_key

        return collections.OrderedDict({
            'sender': public_key,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time})

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def display_transaction(transaction):
        # for transaction in transactions:
        dict = transaction.to_dict()
        print("sender: " + dict['sender'])
        print('-----')
        print("recipient: " + dict['recipient'])
        print('-----')
        print("value: " + str(dict['value']))
        print('-----')
        print("time: " + str(dict['time']))
        print('-----')
