import sys

# Open a given input file and return the values as an array
def getInput(filePath):
    file = open(filePath, 'r')
    content = file.readlines()
    content = [x.strip() for x in content]

    result = []
    for val in content:
        result.append(val)

    return result

# Given a list of values, convert it into a matrix
def toMatrix(values):
  matrix = [[0 for x in range(len(values[0]))] for y in range(len(values))]

  for i in range(len(values)):
    for j in range(len(values[i])):
      matrix[i][j] = values[i][j]

  return matrix

# Given a list, find the least common value within the list
def leastCommonBit(values):
  return str(min(set(values), key=values.count))

# Given a list, find the most common value within the list
def mostCommonBit(values):
  return str(max(set(values), key=values.count))

# Filter the given rows out of a matrix using the given filter value
# on a given column
def filterByMatrixColumn(matrix, filter, column):
  result = matrix

  i = 0
  while i < len(matrix):
    if (filter != matrix[i][column]):
      matrix.pop(i)
    else:
      i += 1

  return result

# Get the oxygen rating from the matrix
def getOxygenRating(matrix):
  i = 0
  while len(matrix) > 1:
    column = [col[i] for col in matrix]

    mostCommon = mostCommonBit(column)
    leastCommon = leastCommonBit(column)

    if (mostCommon == leastCommon):
      mostCommon = '1'

    matrix = filterByMatrixColumn(matrix, mostCommon, i)
    i += 1

  return int(''.join(matrix[0]), 2)

# Get the co2 rating from the matrix
def getCO2Rating(matrix):
  i = 0
  while len(matrix) > 1:
    column = [col[i] for col in matrix]
    mostCommon = mostCommonBit(column)
    leastCommon = leastCommonBit(column)
    if (mostCommon == leastCommon):
      leastCommon = '0'
    matrix = filterByMatrixColumn(matrix, leastCommon, i)
    i += 1

  return int(''.join(matrix[0]), 2)

def main():
  filePath = sys.argv[1]
  
  print('Starting')
  values = getInput(filePath)
  matrix = toMatrix(values)
  oxygen = getOxygenRating(matrix)
  
  values = getInput(filePath)
  matrix = toMatrix(values)
  co2 = getCO2Rating(matrix)

  print('oxygen: ' + str(oxygen))
  print('c02: ' + str(co2))
  print('Result: ' + str(oxygen * co2))

if __name__ == '__main__':
    main()