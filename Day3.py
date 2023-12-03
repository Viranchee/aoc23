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
sampleSolution2 = 467835


class Day3:
  def __init__(self, dir_name):
    self.dir_name = dir_name
  
  def __text__(self):
    text = sample1
    # input_file = str(3) + ".txt"
    # with open(self.dir_name + "/" + input_file, 'r') as f:
    #   text = f.read()
    return text


  def makeDS(self, charMatrix: list[list[int]]):
    numbers = dict[tuple[int, int]: int]() # (i, j) -> val
    specials = dict[tuple[int, int]: int]() # (i, j) -> val

    for i in range(len(charMatrix)):
      number = 0; start = None
      
      for j in range(len(charMatrix[i])):
        val = chr(charMatrix[i][j])
        if val.isdigit():
          if start == None:
            start = (i, j)
          number = number * 10 + int(val)
        else:
          if number != 0:
            numbers[start] = number
          number = 0; start = None
        if not val == '.':
            specials[(i,j)] = 0
      if number != 0:
        # numbers.append((number, start[0], start[1]))
        numbers[start] = number
    
    # print(numbers)
    # print(specials)
    return (numbers, specials)

  def adjacentToSymbol(self, number: int, position: tuple[int,int], specials: dict[tuple[int, int], int]):
    (i, j) = position
    lengthOfVal = len(str(number))
    
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

    adjacentSum = 0
    for position in numbers:
      val = numbers[position]
      if self.adjacentToSymbol(val, position, specials):
        adjacentSum += numbers[position]
    print(adjacentSum)

    sumOfGearRatios = 0
    





if __name__ == "__main__":
  import os
  dir_name = os.path.dirname(__file__)
  Day3(dir_name).solve()
