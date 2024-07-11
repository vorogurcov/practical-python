def getdata(filename):
  data = []
  with open(filename,'rt') as file:
    for line in file:
      line = line[:-1]
      elements = line.split(' ')
      data.append(tuple(elements))
  return data

def getdictionary(filename):
  dict = {}
  with open(filename, 'rt') as file:
    for line in file:
      line = line.split(' ')
      dict[line[0]] = int(line[1])
  return dict

dict = getdictionary('D:\Projects\practical-python\Work\Data\Dictionary.txt')
print(list(enumerate(dict.keys())))
#for pos, name in enumerate(dict.keys()):
#  print(f'{name}\'s position is {pos}')
