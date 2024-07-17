import stock
from stock import Stock

def FuckDown(n):
  while (n > 0):
    yield ('FUCK OFF ' + str(n))
    n-=2

class Player:
  def __init__(self,name,hp,objects):
    self.name = name
    self.hp = hp
    self.objects = list(objects)
  def __iter__(self):
    return self.objects.__iter__()	

def main():
  player = Player('IVAN',100,['penis','huenis','senis'])
  ig = player.__iter__()
  while True:
    try:
      print(next(ig))
    except StopIteration:
      break

  for i in FuckDown(10):
    print(i + str(6))
  
if __name__ == '__main__':
  main()