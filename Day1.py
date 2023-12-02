
class Day1:
  def __init__(self, dir_name: str):

    self.dir_name = dir_name

  def solve(self):
    input_file = str(1) + ".txt"
    text = ""
    with open(self.dir_name + "/" + input_file, 'r') as f:
      text = f.read()
    strToNum = {
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6, 
      'seven': 7,
      'eight': 8,
      'nine': 9
    }
    total = 0
    for line in text.strip().split('\n'):
      # print(line, end=" -> ")
      first = -1; last = 0
      temp = ""
      for char in line:
        digit = None
        if char.isdigit():
          digit = char
        else:
          temp += char
          for (k,v) in strToNum.items():
            if temp.endswith(k):
              digit = str(v)
              line = line.replace(k, digit)
        if digit:
          if first == -1:
            first = int(digit)
          last = int(digit)
      
      line_sum = first * 10 + last
      total += line_sum
      # print(line)

    print("Day1 -> " + str(total))

if __name__ == "__main__":
  import os
  dir_name = os.path.dirname(__file__)
  d1 = Day1(dir_name)
  d1.solve()