def solution():
  import sys
  input = sys.stdin.readline
  
  cnt = 0
  
  N, M = map(int, input().split())
  S = set([input() for _ in range(N)])
  
  for _ in range(M):
    t = input()
    if t in S:
        cnt += 1
        
  print(cnt)