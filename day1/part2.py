import sys

windowSize = 3

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

def sumWindows(windows):
  windowSums = []
  for i in range(len(windows)):
    windowSums.append(sum(windows[i]))

  return windowSums

def getWindows(values, windowSize):
  print('here')
  windows = []
  for i in range(len(values) - windowSize + 1):
    # n to n + windowSize, i.e. windowSize = 3; 2 -> 2 + 3 === 2 -> 5
    windows.append(values[i: i + windowSize]) 

  return windows

def main():
  filePath = sys.argv[1]
  
  print('Starting')
  values = getInput(filePath)

  windows = getWindows(values, windowSize)

  windowSums = sumWindows(windows)

  count = depthIncreasing(windowSums)

  print('Increasing by window: ' + str(count))

if __name__ == '__main__':
    main()