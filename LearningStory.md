## Docstrings

[Google docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)

Using google docstrings allows me to generate documentation for my code.

## Typing: multiple possible typing in python

For annotating multiple possible return types it's possible to use the `Union` class from the python `typing` library:

```Python
from typing import Union


def foo(client_id: str) -> Union[list, bool]
```

Foo can return either a list or a boolean datatype.

[stackoverflow answer](https://stackoverflow.com/a/33945518)

## Public and private keys on a blockchain

_The Private Key is the longer of the two, and is used to generate a signature for each blockchain transaction a user sends out. This signature is used to confirm that the transaction has come from the user, and also prevents the transaction from being altered by anyone once it has been issued. In short, you sign the cryptocurrencies you send to others using a Private Key. If someone were to obtain your private key, they would be able to send your cryptocurrencies to themselves, verifying that transaction with the Private Key — in effect stealing from you!_ ~ [src](https://blog.wetrust.io/why-do-i-need-a-public-and-private-key-on-the-blockchain-c2ea74a69e76)

## PyCryptoDome: RSA

RSA is a public key algorithm.
[PyCryptoDome RSA - docs](https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html)

## PyCryptoDome: PKCS#1 OAEP (RSA)

PKCS-OAEP is an asymmetric cipher based on RSA and OAEP padding. Its used for encrypting messages. In my case it's used for creating a signature attribute for client objects.
[RFC8017](https://datatracker.ietf.org/doc/html/rfc8017#section-7.1)
[PyCryptoDome PKCS#1 OAEP (RSA) - docs](https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html)

## File structure

## Module imports

[How to write an **init**.py/ how to import modules in python](https://towardsdatascience.com/whats-init-for-me-d70a312da583)

# Sources

1. [Develop a blockchain application from scratch in Python](https://gist.github.com/satwikkansal/4a857cad2797b9d199547a752933a715) by [Satwik Kansal](https://gist.github.com/satwikkansal)
2. [Google docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
3. [Python Blockchain](https://www.tutorialspoint.com/python_blockchain/python_blockchain_introduction.htm) from Tutorialspoint.com.
   - NOTE: this tutorial uses [pyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html)
