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

# n = int(input())
# result = list()

# for i in range(n):
#   k = list(map(int,input().split()))
#   matrix = list()
#   for i in range(k[1]):
#     matrix.append([0]*k[0])
#   for i in range(k[2]):
#     q = list(map(int,input().split()))
#     matrix[q[1]][q[0]] = 1
  
#   for i in range(k[1]):
#     for j in range(k[0]):
#       if matrix[i][j] == 1:
#         matrix[i][j] == 2
#         i == 0 j == 0
#         i == 0
#         j == 0
#         i == k[1] j == k[0]
#         i == k[1]
#         j == k[0]
#         bool = matrix[i+1][j] == 1 or matrix[i-1][j] == 1 or matrix[i][j-1] == 1 or matrix[i][j+1] == 1
#         while 
        
  
  

# 1074 도미노

[N, r, c] = list(map(int,input().split()))
result = 0
k = 1
while True:
  if r//2 == 0:
    if r == 0 and c == 0:
      pass
    elif r == 0 and c == 1:
      result = result + 1
    elif r == 1 and c == 0:
      result = result + 2
    elif r == 1 and c == 1:
      result = result + 3  
    break
  if r//2 > 2**(N-k): 
    result = result + 2**(N-k)
  if c//2 > 2**(N-k): 
    result = result + 2**(N-k-1)
  r = r % 2**(N-1)
  c = c % 2**(N-1)
  k = k + 1
  
print(result)
    
  