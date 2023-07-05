def solution():
  import sys
  input = sys.stdin.readline
  students = [False for i in range(30)]
  noSubmitList = []
  for i in range(28):
    n = int(input())
    students[n-1] = True
  for i in range(30):
    if students[i] == False:
      noSubmitList.append(i+1)
  noSubmitList.sort()
  for i in noSubmitList:
    print(i)