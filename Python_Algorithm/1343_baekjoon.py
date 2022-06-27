# 나의 풀이

import sys

board = input()
PLN = list()

count = 0

def appendPLN(count):
  global PLN
  if count == 0:
    pass
  elif count % 2 == 1:
    print(-1)
    sys.exit()
  else: 
    FD = count // 4
    FR = count % 4
    TD = FR // 2
    PLN.append('AAAA'*FD + 'BB'*TD)
    
for k, i in enumerate(board):
  if k == len(board)-1 and i != '.':
    count += 1
    appendPLN(count)
  elif i == '.':
    appendPLN(count)
    PLN.append('.')
    count = 0
  else:
    count += 1

for i in PLN:
  print(i, end="")
  
# 좋은 풀이

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
  print(-1)
    
else:
  print(board)
