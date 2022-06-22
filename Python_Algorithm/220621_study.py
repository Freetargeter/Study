# # 1003 피보나치

# def fibonacci(n):
#   global fibo
#   if (n in fibo.keys()) == True:
#     return fibo[n]
#   else:
#     f1 = fibonacci(n-1)
#     f2 = fibonacci(n-2)
#     p = f1[0] + f2[0]
#     a = f1[1][0] + f2[1][0]
#     b = f1[1][1] + f2[1][1]
#     fibo[n] = [p, [a, b]]
#     return fibo[n]
  
# k = int(input())
# result = list()

# for i in range(k):
#   t = int(input())
#   fibo = {0:[0,[1,0]],1:[1,[0,1]]}
#   f = fibonacci(t)
#   result.append([f[1][0],f[1][1]])

# for i in result:
#   print(i[0],i[1])



# # 1012 유기농 배추

import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        m, n = map(int, input().split())
        matrix[n][m] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)

# 1074 Z

[N, r, c] = list(map(int,input().split()))
result = 0
k = 1

while True:
  if r == 0 and c == 0:
    break
  if r > 2**(N-k)-1: 
    result = result + (2**(N-k))**2*2
  if c > 2**(N-k)-1: 
    result = result + (2**(N-k))**2
  r = r % 2**(N-k)
  c = c % 2**(N-k)
  k = k + 1
  
print(result)
