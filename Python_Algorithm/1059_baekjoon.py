len = int(input())
set = list(map(int,input().split()))
n = int(input())

set.append(0)
set.sort()

iNum = -1

for i, p in enumerate(set):
  if p > n:
    iNum = i -1
    break
  
if set[iNum]-n == 0 or set[iNum+1]-n == 0 or iNum == -1:
  result = 0
else:
  result = (n-set[iNum]) * (set[iNum+1]-n) -1
print(result)



