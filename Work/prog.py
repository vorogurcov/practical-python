from stock import Stock

def main():
  goog = Stock('GOOG',100,490.10)
  goog.cost()
  goog.sell(25)
  goog.cost()
if __name__ == '__main__':
  main()