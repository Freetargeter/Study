fac_list = {0:1, 1:1}

def factorial(n):
  if n in fac_list.keys():
    return fac_list[n]
  else: 
    maxKey = max(fac_list.keys())
    result = fac_list[maxKey]
    for i in range(maxKey+1, n+1):
      fac_list[i] = result * i
      result = result * i
    return fac_list[n]


N = int(input())
reLi = list()

for i in range(N):
  K, C = map(int,input().split())
  result = int(factorial(C)/(factorial(K)*factorial(C-K)))
  reLi.append(result)

for i in reLi:
  print(i)
  

