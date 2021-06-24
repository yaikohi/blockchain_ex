import datetime
import collections
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import binascii


class Transaction:
    """Documents a transaction on the blockchain.

    To instantiate a `transaction` object it requires: a senders' public key, 
    the receivers' public key, and a value that denotes the amount to be transferred.
    All attributes are necessary for instantiation.

    Attributes:
        sender (:obj: client.Client): The senders' public key.
        recipient (:obj: Crypto.PublicKey.RSA.RsaKey): The recipients' public key.
        value (float): The value denoting the amount of crypto to be transferred.

    Example:
        sender1 = Client()
        receiver = Client()
        transaction1 = Transaction(sender, 
                                    receiver1.public_key, 
                                    48.4)
        signature = transaction1.sign_transaction

    """

    def __init__(self,
                 sender: RSA.RsaKey,
                 recipient: RSA.RsaKey,
                 value: float):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self) -> collections.OrderedDict:
        """Creates a dict object of class for display purposes.

        Returns:
            [:obj: collections.OrderedDict]: Transactions' attributes contained in
                 an ordered dictionary object.
        """
        if self.sender == "Genesis":
            public_key = "Genesis"
        else:
            public_key = self.sender.public_key

        return collections.OrderedDict({
            'sender': public_key,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time})

    def sign_transaction(self) -> str:
        """Signs the transaction with the private key of the sender.

        Returns:
            str: The signature for the transaction created with the senders' 
                private key.
        """
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def display_transaction(self):
        """Displays the transaction in the terminal.

        The dictionary object within the received transaction is copied to 
            a temporary variable `dict` and using the dictionary keys, the 
            various values are printed on the console.
        """
        dict = self.to_dict()
        print("sender: " + dict['sender'])
        print('-----')
        print("recipient: " + dict['recipient'])
        print('-----')
        print("value: " + str(dict['value']))
        print('-----')
        print("time: " + str(dict['time']))
        print('-----')
