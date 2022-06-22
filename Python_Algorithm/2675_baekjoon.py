n = int(input())
result = list()

for i in range(n):
  N, st = input().split()
  N = int(N)
  RS = ''
  for j in st:
    RS = RS + j*N
  result.append(RS)

for i in result:
  print(i)