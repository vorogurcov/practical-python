class Stock:

  def __init__(self,name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price
  
  def sell(self,count):
    self.shares -=count
    print(self.shares)

  def cost(self):
    print( self.shares * self.price )