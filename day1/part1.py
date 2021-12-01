import sys

# Open a given input file and return the values as an array
def getInput(filePath):
    file = open(filePath, 'r')
    content = file.readlines()
    content = [x.strip() for x in content]

    result = []
    for val in content:
        result.append(int(val))

    return result

# Given an list of values return a count of the values that 
# increased over the previous value
def depthIncreasing(values):
  count = 0
  for i in range(len(values) - 1):
    if values[i] < values[i+1]:
      count += 1

  return count

def main():
    filePath = sys.argv[1]
    print('Starting')
    count = depthIncreasing(getInput(filePath))
    print('Increasing: ' + str(count))

if __name__ == '__main__':
    main()