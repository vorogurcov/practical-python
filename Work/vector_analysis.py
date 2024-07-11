#Get modules + find collinear vectors
import math

def getpoints(filename):
  points = []
  with open(filename,"rt") as file:
    next(file)
    for line in file:
      line = line.split(' ')
      points.append((float(line[0]),float(line[1])))
  return points

def getmodules(points):
  modules = []
  for point in points:
    modules.append(math.sqrt(point[0] * point[0] + point[1] * point[1]))
  return modules

points = getpoints("D:\Projects\practical-python\Work\Data\points.txt")
modules = getmodules(points)

for point,module in zip(points,modules):
  print(f'The point with coordinates: {point} has the following module: {module:.3f}')

col_vect = []
for index,point in enumerate(points):
  for next_point in points[index + 1:]:
    if(point[0] / next_point[0] == point[1] / next_point[1]):
      col_vect.append((point,next_point)) 

print('Collinear vectors are: \n',col_vect)