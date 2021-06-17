class User:
    """A user with a unique id, a name, and a balance containing currency.
    
    -- TODO: add extra info here --
    
    Attributes:
        id: a unique key id for specifying the user
        name: the name of the user
        balance: a value describing the currency available to the user
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