import sys
import fileinput
import numpy as np

def getInput(filePath):
  content = []
  input = fileinput.input(files=(filePath), mode='r')
  for line in input:
    content.append(line.rstrip())

  return content

def getVectors(A, B):
  vector = []

  Xstart = A[0]
  Xstop = B[0]
  Xstep = 1
  if Xstart == Xstop:
    Xstep = 0
  elif Xstop - Xstart < 1:
    Xstep = -1

  Ystart = A[1]
  Ystop = B[1]

  Ystep = 1
  if Ystart == Ystop:
    Ystep = 0
  elif Ystop - Ystart < 1:
    Ystep = -1

  length = max(abs(Xstop - Xstart),  abs(Ystop - Ystart)) + 1

  x = Xstart
  y = Ystart
  for i in range(length):
    vector.append([x, y])
    x += Xstep
    y += Ystep

  return vector
  
def main():
  filePath = sys.argv[1]
  input = getInput(filePath)

  maxX = 1000
  maxY = 1000
  matrix = np.zeros((maxX, maxY))

  for i in range(len(input)):
    points = [x.split(',') for x in input[i].split(' -> ')]
    A = [[int(x[0]), int(x[1])] for x in points]

    if A[0][0] == A[1][0]:
      print('horizontal')
      vector = getVectors(A[0], A[1])
      for j in range(len(vector)):
        matrix[vector[j][0]][vector[j][1]] += 1
        
    elif A[0][1] == A[1][1]:
      vector = getVectors(A[0], A[1])
      for k in range(len(vector)):
        matrix[vector[k][0]][vector[k][1]] += 1
        
    else:
      print('diagonal')
      vector = getVectors(A[0], A[1])
      for k in range(len(vector)):
        matrix[vector[k][0]][vector[k][1]] += 1

  values = np.array(matrix).flatten()
  sum = 0
  for i in values:
    if i > 1:
      sum += 1
  print('Result: ' + str(sum))


if __name__ == '__main__':
    main()