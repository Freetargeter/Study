# import sys

# n = int(input())
# li = list(map(int, input().split()))
# max = -sys.maxsize
# min = sys.maxsize

# for i in range(len(li)):
#   if li[i] > max :
#     max = li[i]
#   if li[i] < min :
#     min = li[i]
    
# print(min, max)


# import sys

# order = 0
# max = -sys.maxsize

# for i in range(9):
#   a = int(input())
#   if max < a :
#     max = a
#     order = i
# print(max)
# print(order+1)


# a = int(input())
# b = int(input())
# c = int(input())
# n = str(a*b*c)
# li = [0,0,0,0,0,0,0,0,0,0]
# for i in range(len(n)):
#   k = int(n[i])
#   li[k] = li[k] + 1
# for i in range(10):
#   print(li[i])


# s = set()

# for i in range(10):
#   a = int(input())
#   if a%42 not in s:
#     s.add(a%42)

# print(len(s))

import sys

n = int(sys.stdin.readline())
max = -sys.maxsize
sum = 0
li = list(map(int,sys.stdin.readline().split()))

for i in range(n):
  if max < li[i]:
    max = li[i]

for i in range(n):
  sum = sum + li[i]*100/max
print(sum)
print(sum/n);