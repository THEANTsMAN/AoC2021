import sys
import fileinput
import numpy as np

def getInput(filePath):
  content = []
  input = fileinput.input(files=(filePath), mode='r')
  for line in input:
    content.append(line.rstrip())

  return content
  
def main():
  filePath = sys.argv[1]
  input = getInput(filePath)

  maxX = 1000
  maxY = 1000
  matrix = np.zeros((maxX, maxY))

  for i in range(len(input)):
    points = [x.split(',') for x in input[i].split(' -> ')]
    A = [x for x in points]

    if A[0][0] == A[1][0]:
      # print('horizontal')
      step = 1
      if int(A[1][1]) - int(A[0][1]) < 1:
        step = -1
      
      start = int(A[0][1])
      stop = int(A[1][1])

      vector = [[int(A[0][0]), x] for x in range(start, stop + step, step)]
      for j in range(len(vector)):
        matrix[vector[j][0]][vector[j][1]] += 1
        

    elif A[0][1] == A[1][1]:
      # print('vertical')
      step = 1
      if int(A[1][0]) - int(A[0][0]) < 1:
        step = -1
    
      start = int(A[0][0])
      stop = int(A[1][0])

      vector = [[x, int(A[0][1])] for x in range(start, stop + step, step)]
      print(vector)
      for k in range(len(vector)):
        matrix[vector[k][0]][vector[k][1]] += 1
        
    else:
      # print('diagonal')
      Xstart = int(A[0][0])
      Xstop = int(A[1][0])
      Xstep = 1
      if Xstop - Xstart < 1:
        Xstep = -1

      Ystart = int(A[0][1])
      Ystop = int(A[1][1])
      Ystep = 1
      if Ystop - Ystart < 1:
        Ystep = -1

      vector = []
      length = abs(Xstop - Xstart)
      lengthY = abs(Ystop - Ystart)

      if (length != lengthY):
        print('lengths')

      x = Xstart
      y = Ystart

      for i in range(length):
        vector.append([x, y])
        x += Xstep
        y += Ystep

      print(vector)
      for k in range(len(vector)):
        matrix[vector[k][0]][vector[k][1]] += 1

    # print('\n')



  # print(matrix)
  values = np.array(matrix).flatten()
  sum = 0
  for i in values:
    if i > 1:
      sum += 1
  print('Result: ' + str(sum))


if __name__ == '__main__':
    main()