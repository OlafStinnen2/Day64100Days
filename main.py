class bankaccount:
  customer_id = None
  name = None
  value = None

  def __init__(self, customer_id, name, value):
    self.customer_id = customer_id
    self.name = name
    self.value = value


  def transfer(self, amount):
    if amount >= 0:
      print(self.value)
      self.value += amount
    else:
      if self.value < abs(amount):
        print("To little money on bank account")
      else:
        self.value += amount
        

        



Olaf_Start = bankaccount("Olaf100", "Olaf Stinnen",100.01)
Olaf_Start.value += 100
Olaf_Start.transfer(-300)
print(Olaf_Start.value)



