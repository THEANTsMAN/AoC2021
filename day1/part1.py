import sys

def getInput(filePath):
    file = open(filePath, 'r')
    content = file.readlines()
    content = [x.strip() for x in content]

    result = []
    for val in content:
        result.append(int(val))

    return result

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