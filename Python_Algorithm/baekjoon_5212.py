def solution():
  import sys
  input = sys.stdin.readline
  import copy
  
  R, C = map(int, input().split())
  MAP = []
  for i in range(R):
    MAP.append(list(input()))
  
  changedMap = copy.deepcopy(MAP)
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  for i in range(R): 
    for j in range(C):
      if MAP[i][j] == ".": continue
      cnt = 0
      for k in range(4):
        nx = i+dx[k]; ny = j+dy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
          cnt += 1
          continue
        elif MAP[nx][ny] == ".": cnt += 1
      if cnt >= 3:
        changedMap[i][j] = "."
  
  start_row = 0
  end_row = R - 1   
  start_col = 0
  end_col = C - 1 
    
  for i in range(R):
    if "X" in changedMap[i]: 
      start_row = i
      break
    
  for i in reversed(range(R)):
    if "X" in changedMap[i]: 
      end_row = i
      break
  
  def findStartCol():
    nonlocal start_col
    for i in range(C):
      for j in range(R):
        if changedMap[j][i] == "X":
          start_col = i
          return  
        
  def findEndCol():
    nonlocal end_col
    for i in reversed(range(C)):
      for j in range(R):
        if changedMap[j][i] == "X":
          end_col = i
          return
  
  findStartCol(); findEndCol();
  
  for i in range(start_row, end_row+1):
    for j in range(start_col, end_col+1):
      print(changedMap[i][j], end="")
    print()
    
        