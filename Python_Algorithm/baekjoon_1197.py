def solution():
  import sys
  input = sys.stdin.readline

  V, E = map(int, input().split())
  matrix = [[0]*V for _ in range(V)]

  for _ in range(E):
    A, B, C = map(int, input().split())
    matrix[A-1][B-1] = C
    matrix[B-1][A-1] = C

  if V == 1:  
    print(matrix[0][1])
    return
    
  # 집합에 포함된 정점은 리스트에 넣는다.
  # 집합에 안 포함되었으며 집합에 포함된 정점에서 1개 간선으로 갈 수 있는 경로가 있는 정점을 검사하며 
  # 하나씩 포함시킨다.

  group = [0 for _ in range(V+1)]
  included = 2
  group[1] = 1
  SOW = 0
  min = sys.maxsize 
  minIdx = sys.maxsize

  for i, v in enumerate(matrix[0]):
    if v != 0 and v < min:
      minIdx = i
      min = v
      
  group[minIdx+1] = 1
  SOW += v

  while True:
    if included==V: break
    
    min = sys.maxsize
    minIdx = sys.maxsize
    
    for idx in range(1, V+1):
      if group[idx] == 0:
        for i, v in enumerate(matrix[idx-1]):
          if group[i+1] == 0 and v < min:
            min = v
            minIdx = i
    group[minIdx+1] = 1
    included += 1
    SOW += min

  print(SOW)
    
      
  