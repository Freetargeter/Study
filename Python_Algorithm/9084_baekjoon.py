# dynamic programming
import sys
input = sys.stdin.readline

t = int(input())
resultWay = list()

for i in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())
    dp = [0 for i in range(m + 1)]
    dp[0] = 1
    for i in c:
        for j in range(i, m + 1):
            dp[j] += dp[j - i]
    resultWay.append(dp[m])

for v in resultWay:  
  print(v)
""" // 재귀 이용 풀이, 시간 초과
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

t = int(input())

def wayByCoin(Coin, M, k):
  global way
  if len(Coin) == k+1:
    if M % Coin[k] == 0:
      way += 1
      return
    else:
      return
  while True:
    wayByCoin(Coin, M, k+1)
    M -= Coin[k]
    if M < 0:
      return
    elif M == 0:
      way += 1
      return 

resultWay = list()

for _ in range(t):
  n = int(input())
  coin = list(map(int,input().split()))
  m = int(input())
  way = 0
  wayByCoin(coin, m, 0)
  resultWay.append(way)

for v in resultWay:  
  print(v)
"""