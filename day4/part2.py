import sys
import fileinput
import numpy

# Open a given input file and return the values as an array
def getInput(filePath):
    bingoNumbers = []
    matrices = []
    temp = []
    input = fileinput.input(files=(filePath), mode='r')
    for line in input:
      if (fileinput.isfirstline()):
        bingoNumbers = map(int, line.split(','))
      else:
        temp.append(line)

    matIdx = -1
    for i in range(len(temp)):
      if temp[i] != '\n':
        matrices[matIdx].append(map(int, temp[i].rstrip().split()))
      else:
        matIdx += 1
        matrices.append([])

    input.close()
    npMatrices = []
    for j in range(len(matrices)):
      npMatrices.append(numpy.array(matrices[j]))

    return [bingoNumbers, npMatrices]
    
def checkWin(matrix, numbers):
  dimensions = numpy.shape(matrix)

  transpose = numpy.transpose(matrix)

  for i in range(dimensions[0]):
    if (set(matrix[i]).issubset(numbers) or set(transpose[i]).issubset(numbers)):
      return True

  return False

def play(matrix, bingoNumbers):
  numbers = []
  lastMatrix = matrix
  win = len(matrix)
  
  while win > 0:
    numbers.append(bingoNumbers.pop(0))
    j = 0
    while j < len(matrix):
      if(checkWin(matrix[j], numbers)):
        if (win > 1):
          win -= 1
          lastMatrix.pop(j)
        else:
          return [numbers, lastMatrix, j]

      j += 1

  return [lastMatrix, numbers, win]
        

def main():
  filePath = sys.argv[1]
  
  print('Starting')
  [bingoNumbers, matrices] = getInput(filePath)
  [winNumbers, winMatrix, winner] = play(matrices, bingoNumbers)
   
  print(winMatrix)
  print(winNumbers)

  sum = numpy.sum(numpy.setdiff1d(numpy.ravel(winMatrix), winNumbers)) * winNumbers[-1]
  print(sum)

if __name__ == '__main__':
    main()