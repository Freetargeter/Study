# for i in range(2):
#   print("강한친구 대한육군")

# print("         ,r\'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")

# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# a = input()
# print(a, "??!", sep="")

# R = []
# while True :
#   a, b = map(int, input().split())
#   if a==0 and b==0:
#     break
#   R.append(a+b)
# for i in range(len(R)):
#   print(R[i])
  
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break
n = 0
c = int(input())
a = c
b = 20
while True:
  if a < 10 :
    b = 10*a + a
  else :
    b = (a%10)*10 + (a%10+a//10)%10
  a = b
  n = n + 1
  if c == b:
    break
print(n)

# n = int(input())
# num = n
# cnt = 0

# while True:
#   a = num // 10
#   b = num % 10
#   c = (a+b) % 10
#   num = (b+10)+ c
  
#   cnt = cnt + 1
#   if(num == n):
#     break
# print(cnt)
  