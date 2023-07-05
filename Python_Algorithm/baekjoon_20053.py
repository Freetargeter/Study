def solution():
  import sys
  input = sys.stdin.readline
  
  n = int(input())
  
  for _ in range(n):
    _ = int(input())
    li = list(map(int, input().split()))
    print(min(li), end=" ")
    print(max(li))