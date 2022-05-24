# print(ord(input()))

# n = int(input())
# num = list(map(int,list(input())))
# sum = 0

# for i in range(n):
#   sum = sum + num[i]

# print(sum)


a = list(input())
b = dict()

for i in range(len(a)):
  if a[i] not in b:
    b[a[i]] = i

for i in range(97,123,1):
  if chr(i) in b:
    print(b[chr(i)],end=" ")
  else :
    print(-1,end=" ")