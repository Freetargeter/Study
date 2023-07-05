def solution():
  import sys
  input = sys.stdin.readline
  
  n = int(input())
  matrix = [list(map(int, input().split())) for _ in range(n)]
  
  def pooling(matrix):
    pooling_matrix = [[0 for _ in range(len(matrix)//2)] for _ in range(len(matrix)//2)]
    if len(matrix) == 1:
      print(matrix[0][0])
      return
    for i in range(0, len(matrix), 2):
      for j in range(0, len(matrix), 2):
        temp_li = [matrix[i][j], matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]]
        temp_li.sort()
        pooling_matrix[i//2][j//2] = temp_li[2]
    pooling(pooling_matrix)
    
  pooling(matrix)