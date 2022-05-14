# a, b = input().split()
# a = int(a)
# b = int(b)
# if a < b :
#   print("<")
# elif a > b :
#   print(">")
# elif a == b :
#   print("==")

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력
# score = int(input())
# if score >= 90 and score <=100 :
#   print("A")
# elif score >= 80 and score <=89 :
#   print("B")
# elif score >= 70 and score <=79 :
#   print("C")
# elif score >= 60 and score <=69 :
#   print("D")
# else :
#   print("F")

# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# year = int(input())
# if year % 4 == 0:
#   if year % 400 == 0:
#     print("1")
#   elif year % 100 != 0:
#     print("1")
#   else :
#     print("0")
# else :
#   print("0")

# 주어진 점이 어느 사분면에 속하는지 알아내는 것
# x = int(input())
# y = int(input())
# if x > 0 and y > 0 :
#   print("1")
# elif x < 0 and y > 0 :
#   print("2")
# elif x < 0 and y < 0 :
#   print("3")
# else :
#   print("4")

# 알람을 45분전으로 고치기
# h, m = input().split()
# h = int(h)
# m = int(m)

# if m >= 45:
#   print(h, m-45)
# else :
#   if h == 0:
#     print(23, m+15)
#   else :
#     print(h-1, m+15)

# 인공오븐 시간 계산(2525)
# h, m  = input().split()
# tt = int(input())
# h = int(h)
# m = int(m)

# if m + tt >= 60:
#   h = h + (m+tt)//60
#   m = (m+tt)%60
#   if h >= 24:
#     print(h%24, m)
#   else:
#     print(h, m)
# else :
#   m = (m+tt)%60
#   if h >= 24:
#     print(h%24, m)
#   else:
#     print(h, m)

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a==b and b==c:
  print(10000+a*1000)
elif a==b:
  print(1000+a*100)
elif b==c:
  print(1000+b*100)
elif c==a:
  print(1000+c*100)
else:
  if a >= b and a >= c:
    print(a*100)
  elif b >= c and b >= a:
    print(b*100)
  else:
    print(c*100)