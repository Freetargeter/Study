n = int(input())

FD = n // 5
FR = n % 5

if n == 1 or n == 3:
  print(-1)
elif FR % 2 == 0:
  print(FD + FR // 2)
else:
  TD = (FR + 5) // 2
  print(FD + TD - 1)
  

