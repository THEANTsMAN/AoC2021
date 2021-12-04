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
  win = False
  while not win:
    numbers.append(bingoNumbers.pop(0))
    for j in range(len(matrix)):
      if(checkWin(matrix[j], numbers)):
        win = True
        return [numbers, matrix[j], j]

def main():
  filePath = sys.argv[1]
  
  print('Starting')
  [bingoNumbers, matrices] = getInput(filePath)
  [winNumbers, winMatrix, winner] = play(matrices, bingoNumbers)
   
  print(winMatrix)
  print(winNumbers)

  result = numpy.sum(numpy.setdiff1d(winMatrix.ravel(), winNumbers)) * winNumbers[-1]
  print('Result: ' + str(result))

if __name__ == '__main__':
    main()