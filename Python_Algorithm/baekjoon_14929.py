def solution():
  import sys
  
  input = sys.stdin.readline
  n = int(input())
  x = list(map(int, input().split()))
  
  sum = 0
  res = 0
  for i in range(n-1):
    res += x[n-i-1]
    sum += x[n-i-2] * res
  
  print(sum)   