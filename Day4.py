from lark import Lark, Transformer

sample1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
s1 = [8,2,2,1,0,0]
s2 = 467835

class TreeToDict(Transformer):
  def statement(self, items):
    return items[0].children[0].value
    
  def gamenumber(self, items):
    val = items[0].children[0].value
    return int(val)

  def have(self, items):
    haves = []
    for item in items:
      for token in item.iter_subtrees():
        val = token.children[0].value
        haves.append(int(val))  
    return haves
  def winning(self, items):
    winning = []
    for item in items:
      for token in item.iter_subtrees():
        val = token.children[0].value
        winning.append(int(val))  
    return winning

class Day4:
  def __init__(self):
    import os
    self.dir_name = os.path.dirname(__file__)
    grammar_file = self.dir_name + "/Day4.lark"
    with open(grammar_file, 'r') as f:
      self.grammar = f.read()
    self.parser = Lark(self.grammar, parser='lalr')
  
  def __text__(self):
    text = sample1
    # input_file = str(4) + ".txt"
    # with open(self.dir_name + "/" + input_file, 'r') as f:
    #   text = f.read()
    return text

  def part1(self):
    text = self.__text__()
    for line in text.splitlines():
      tree = self.parser.parse(line)
      parsed = TreeToDict().transform(tree).children
      game_number = parsed[0]
      have = parsed[1]
      winning = parsed[2]

      
  def part2(self):
    print("unimplemented")

if __name__ == "__main__":
  d4 = Day4()
  d4.part1()
  # d4.part2()
