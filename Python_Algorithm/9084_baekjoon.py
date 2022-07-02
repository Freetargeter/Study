import sys
input = sys.stdin.readline

t = int(input())

def wayByCoin(Coin, M, k):
  global way
  if len(Coin) == k+1:
    if M % Coin[k] == 0:
      return way + 1
    else:
      return way
  while True:
    M -= Coin[k]
    wayByCoin(Coin, M, k+1)
    if M < 0:
      return way
    elif M == 0:
      return way + 1

for _ in range(t):
  n = int(input())
  coin = list(map(int,input().split()))
  m = int(input())
