def solution():
  import sys
  input = sys.stdin.readline
  
  N = int(input())
  confetti = [list(map(int, input().split())) for _ in range(N)]
  
  result = [0, 0]
  
  def getWhiteBlueConfetti(x, y, N):
    color = confetti[x][y]
    for i in range(x, x+N) :
      for j in range(y, y+N) :
        if color != confetti[i][j] :
          getWhiteBlueConfetti(x, y, N//2)
          getWhiteBlueConfetti(x, y+N//2, N//2)
          getWhiteBlueConfetti(x+N//2, y, N//2)
          getWhiteBlueConfetti(x+N//2, y+N//2, N//2)
          return
    if color == 0 :
      result[0] += 1
    else :
      result[1] += 1
      
  getWhiteBlueConfetti(0, 0, N)
  print(result[0])
  print(result[1])
      
      
    