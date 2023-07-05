import sys
import math

input = sys.stdin.readline

def cf(n1, n2):
  while(n1 != n2):
    if n2 > n1: n1, n2 = n2, n1
    n1 = n1 - n2
  return n1

def cff(n):
  if n == 1: return [1]
  li1 = []
  li2 = []
  for i in range(1,n):
    if i ** 2 > n: break
    elif i ** 2 == n: li1.append(i)
    elif n % i == 0:
      li1.append(i)
      li2.append(int(n/i))
    
  for i in reversed(li2):
    li1.append(i)
  return li1

n = int(input())
nn = list(map(int, input().split()))

if n == 2:
  ansli = cff(cf(nn[0], nn[1]))
if n == 3:
  pa = cf(nn[0], nn[1])
  ansli = cff(cf(pa, nn[2]))

for i in ansli:
  print(i)



