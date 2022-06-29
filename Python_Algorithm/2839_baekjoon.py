import sys
N = int(input())
FD = N // 5
FR = N % 5

while True:
  if FR % 3 == 0:
    print(FD + FR // 3)
    sys.exit()
  else:
    FD -= 1
    FR += 5
    if FD < 0:
      print(-1)
      sys.exit()