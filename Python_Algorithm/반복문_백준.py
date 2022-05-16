#N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. (2739)

# N = int(input())
# for i in range(1,10):
#   print(N, "*",i, "=",i*N)

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.(10950)

# n = int(input())
# a = []
# b = []
# for i in range(n):
#   x, y = input().split()
#   a.append(int(x))
#   b.append(int(y))
# for i in range(n):
#   print(a[i]+b[i])

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#   sum += i
# print(sum)

# import sys

# n = int(input())
# for i in range(n):
#   x, y = map(int, sys.stdin.readline().split())
#   print(x+y)

# n = int(input())
# for i in range(n):
#   print(n-i)
  
# n = int(input())
# a = []
# b = []
# for i in range(n):
#   x, y = input().split()
#   a.append(int(x))
#   b.append(int(y))
# for i in range(n):
#   print("Case #", i+1,": ",a[i]," + ",b[i]," = ", a[i]+b[i],sep="")


# n = int(input())
# for i in range(n):
#   for j in range(n-i-1):
#     print(" ",end="")
#   for j in range(i+1):
#     print("*",end="")
#   print("")

n, x = map(int,input().split())
num = list(map(int,input().split()))

for i in range(n):
  if num[i]< x :
    print(num[i],end=" ")

