FiboList = {0:0,1:1}

def fibonacci(n):
  global FiboList
  if n in FiboList.keys():
    return FiboList[n]
  else:
    FiboList[n] = fibonacci(n-1) + fibonacci(n-2)
    return FiboList[n]
    
N = int(input())
print(fibonacci(N))

