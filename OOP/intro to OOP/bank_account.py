class BankAccount:
  # todo: Add class attribute here
  bank_name = "Python National Bank"
  
  def __init__(self, initial_value=0):
    self.balance = initial_value
    pass
  
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
    else:
      print("Amount must be higher than 0")
  
  def withdraw(self, amount):
    self.balance -= amount
  
  def get_balance(self):
    return self.balance