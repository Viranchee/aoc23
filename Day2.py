sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

class Day2:
  def __init__(self, dir_name):
    self.dir_name = dir_name
    self.allowedRGB = {"red": 12, "green": 13, "blue": 14}

  def __text__(self):
    input_file = str(2) + ".txt"
    text = sample
    with open(self.dir_name + "/" + input_file, 'r') as f:
      text = f.read()
    return text
  

  
  def getLineNoAndLocalMaxima(self, line:str) -> (int, dict[str, int]):
    parts = line.split(': ')
    gameNo = int(parts[0].replace('Game ', ''))
    games = parts[1].split('; ')
    
    localRGBMax = {"red": 0, "green": 0, "blue": 0}
    for game in games:
      rolls = game.split(', ')
      for roll in rolls:
        for color, count in localRGBMax.items():
          if color in roll:
            localRGBMax[color] = max(count, int(roll.replace(color, '')))
    
    return gameNo, localRGBMax

  def solve(self):
    self.total = 0
    self.maxima = 0

    for line in self.__text__().splitlines():
      gameNo, localRGBMax = self.getLineNoAndLocalMaxima(line)
      localMaxima = 1
      
      for color, value in localRGBMax.items():
        localMaxima *= value
        if localRGBMax[color] > self.allowedRGB[color]:
          gameNo = 0
      
      self.total += gameNo
      self.maxima += localMaxima
      
    print("Part 1: ", str(self.total) + "\tPart2: " + str(self.maxima))


if __name__ == "__main__":
  import os
  dir_name = os.path.dirname(__file__)
  Day2(dir_name).solve()