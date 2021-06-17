
"""
File for testing modules.
"""


from client import * 

Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()

transactions = []

t1 = Transaction(
   Dinesh,
   Ramesh.public_key,
   15.0
)

t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(
   Dinesh,
   Seema.public_key,
   6.0
)

t2.sign_transaction()
transactions.append(t2)

t3 = Transaction(
   Ramesh,
   Vijay.public_key,
   2.0
)
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(
   Seema,
   Ramesh.public_key,
   4.0
)
t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(
   Vijay,
   Seema.public_key,
   7.0
)
t5.sign_transaction()
transactions.append(t5)
t6 = Transaction(
   Ramesh,
   Seema.public_key,
   3.0
)
t6.sign_transaction()
transactions.append(t6)
t7 = Transaction(
   Seema,
   Dinesh.public_key,
   8.0
)
t7.sign_transaction()
transactions.append(t7)
t8 = Transaction(
   Seema,
   Ramesh.public_key,
   1.0
)
t8.sign_transaction()
transactions.append(t8)
t9 = Transaction(
   Vijay,
   Dinesh.public_key,
   5.0
)
t9.sign_transaction()
transactions.append(t9)
t10 = Transaction(
   Vijay,
   Ramesh.public_key,
   3.0
)
t10.sign_transaction()
transactions.append(t10)

def display_transaction(transaction):
    # for transaction in transactions:
    dict = transaction.to_dict()
    print ("sender: " + dict['sender'])
    print ('-----')
    print ("recipient: " + dict['recipient'])
    print ('-----')
    print ("value: " + str(dict['value']))
    print ('-----')
    print ("time: " + str(dict['time']))
    print ('-----')


for transaction in transactions:
    display_transaction(transaction)
    print ('--------------')