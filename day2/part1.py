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

# Given a list of values, compute the final position
def getPosition(values):
  horizontal = 0
  depth = 0

  for i in range(len(values)):
    data = values[i].split()
    if (data[0] == 'forward'):
      horizontal += int(data[1])
    elif (data[0] == 'down'):
      depth += int(data[1])
    elif (data[0] == 'up'):
      depth -= int(data[1])

  return horizontal * depth

def main():
  filePath = sys.argv[1]
  
  print('Starting')
  values = getInput(filePath)
  result = getPosition(values)

  print('Result: ' + str(result))

if __name__ == '__main__':
    main()