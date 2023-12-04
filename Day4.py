from lark import Lark, Transformer

sample1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
s1 = 25183
s2 = 30

class TreeToDict(Transformer):
  def games(self, items):
    return items
  
  def game(self, items):
    theGame = (items[0], items[1], items[2])
    return theGame
    
  def gamenumber(self, items):
    item = items[0]
    val = int(items[0].children[0].value)
    return val

  def have(self, items):
    haves = set()
    for item in items:
      for token in item.iter_subtrees():
        val = token.children[0].value
        haves.add(int(val))  
    return haves
  def winning(self, items):
    winning = set()
    for item in items:
      for token in item.iter_subtrees():
        val = token.children[0].value
        winning.add(int(val))  
    return winning

class Day4:
  def __init__(self):
    import os
    dir_name = os.path.dirname(__file__)
    grammar_file = dir_name + "/Day4.lark"
    text = sample1
    input_file = str(4) + ".txt"
    with open(dir_name + "/" + input_file, 'r') as f:
      text = f.read()
    with open(grammar_file, 'r') as f:
      grammar = f.read()
      parser = Lark(grammar, parser='lalr')
    # for line in text.splitlines():
    #   tree = self.parser.parse(line)
    #   game = TreeToDict().transform(tree).children[0]
    #   print(game)
    tree = parser.parse(text)
    self.games = TreeToDict().transform(tree).children[0]
  

  def part1(self):
    points = 0
    for game in self.games:
      score = 1
      for have in game[1]:
        if have in game[2]:
          score <<= 1
      score >>= 1
      points += score
    print(points)
      
  def part2(self):
    won = [0] * len(self.games)
    for game in self.games:
      for have in game[1]:
        if have in game[2]:
    
    total = sum(total_cards)
    print(total)



if __name__ == "__main__":
  d4 = Day4()
  d4.part1()
  d4.part2()
