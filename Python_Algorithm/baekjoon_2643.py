def solution():
  import sys
  input = sys.stdin.readline
  N = int(input())
  paper = [list(map(int, input().split())) for _ in range(N)] 

  white_paper = 0
  blue_paper = 0

  def solution(x, y, N) :
    nonlocal white_paper
    nonlocal blue_paper
    color = paper[x][y]
    for i in range(x, x+N) :
      for j in range(y, y+N) :
        if color != paper[i][j] :
          solution(x, y, N//2)
          solution(x, y+N//2, N//2)
          solution(x+N//2, y, N//2)
          solution(x+N//2, y+N//2, N//2)
          return
    if color == 0 :
      white_paper += 1
    else :
      blue_paper += 1


  solution(0,0,N)
  print(white_paper)
  print(blue_paper)
  # print(result.count(0))
  # print(result.count(1))