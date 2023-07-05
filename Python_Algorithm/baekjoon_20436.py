def solution():
  
  keyboard = ["qwertyuiop",
              "asdfghjkl",
              "zxcvbnm"]
  consonant = "qwertasdfgzxcv"
    
  def findLoc(x):
    for i, v in enumerate(keyboard):
      if x in v: return [i, v.index(x)]
      
  def calcLocDiff(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
      
  firstLeft, firstRight = input().split()
  prevLocL = findLoc(firstLeft); prevLocR = findLoc(firstRight)
  string = input()
  cnt = 0

  for i in string:
    presLoc = findLoc(i)
    if i in consonant:
      cnt += calcLocDiff(presLoc, prevLocL) + 1
      prevLocL = presLoc
    else:
      cnt += calcLocDiff(presLoc, prevLocR) + 1
      prevLocR = presLoc

  print(cnt)
    
  
  