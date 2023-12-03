sample1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
sampleSolution1 = 4361
arr = [467, 35, 633, 617, 592, 755, 664, 598]

sample2 = ""

class Day3:
  def __init__(self, dir_name):
    self.dir_name = dir_name
  
  def __text__(self):
    input_file = str(3) + ".txt"
    text = sample1
    with open(self.dir_name + "/" + input_file, 'r') as f:
      text = f.read()
    return text


  def makeDS(self, charMatrix: list[list[int]]):
    numbers = [] # (val, (i,j))
    specials = dict() # (i, j) -> val

    for i in range(len(charMatrix)):
      number = 0; start = None
      
      for j in range(len(charMatrix[i])):
        val = chr(charMatrix[i][j])
        if val.isdigit():
          if start == None:
            start = (i, j)
          number = number * 10 + int(val)
        elif val == '.':
          if number != 0:
            numbers.append((number, start[0], start[1]))
          number = 0; start = None
        else:
          if number != 0:
            numbers.append((number, start[0], start[1]))
          number = 0; start = None
          specials[(i,j)] = val
      if number != 0:
        numbers.append((number, start[0], start[1]))
    
    print(numbers)
    print(specials)

    return (numbers, specials)

  def isValid(self, number: tuple[int, int, int], specials: dict[tuple[int, int], int]):
    (val, i, j) = number
    lengthOfVal = len(str(val))
    
    # i and j box
    iUp = i - 1
    iDown = i + 1
    jLeft = j - 1
    jRight = j + lengthOfVal
    # same line check
    if (i, jRight) in specials or (i, jLeft) in specials:
      return True
    # up and down check
    for k in range(lengthOfVal + 2):
      if (iUp, jLeft + k) in specials or (iDown, jLeft + k) in specials:
        return True
      
    

  def solve(self):
    x = '@'
    # get ascii value of x
    asciix = ord(x)
    # convert back to char
    charx = chr(asciix)

    matrix = self.__text__().splitlines()
    length = len(matrix)
    width = len(matrix[0])

    charMatrix = [[0 for x in range(width)] for y in range(length)]
    
    # Traditional for loop
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        val = matrix[i][j]
        charMatrix[i][j] = ord(val)

    (numbers, specials) = self.makeDS(charMatrix)
    sum = 0
    for number in numbers:
      if self.isValid(number, specials):
        sum += number[0]
    print(sum)





if __name__ == "__main__":
  import os
  dir_name = os.path.dirname(__file__)
  Day3(dir_name).solve()
