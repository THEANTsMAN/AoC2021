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

# Given a list, find the least common value within the list
def leastCommonBit(values):
  return str(min(set(values), key=values.count))

# Given a list, find the most common value within the list
def mostCommonBit(values):
  return str(max(set(values), key=values.count))

# Given a matrix, find the gamma value
def getGamma(matrix):
  gamma = []
  for i in range(len(matrix[0])):
    column = [col[i] for col in matrix]
    gamma.append(mostCommonBit(column))

  return int(''.join(gamma), 2)

# Given a matrix, find the epsilon value
def getEpsilon(matrix):
  epsilon = []
  for i in range(len(matrix[0])):
    column = [col[i] for col in matrix]
    epsilon.append(leastCommonBit(column))

  return int(''.join(epsilon), 2)

# Given a list of values, convert it into a matrix
def toMatrix(values):
  matrix = [[0 for x in range(len(values[0]))] for y in range(len(values))]

  for i in range(len(values)):
    for j in range(len(values[i])):
      matrix[i][j] = values[i][j]

  return matrix

def main():
  filePath = sys.argv[1]
  
  print('Starting')
  input = getInput(filePath)
  matrix = toMatrix(input)
  
  gamma = getGamma(matrix)
  epsilon = getEpsilon(matrix)
  print(gamma)
  print(epsilon)

  result = gamma * epsilon
  print('Result: ' + str(result))


if __name__ == '__main__':
    main()