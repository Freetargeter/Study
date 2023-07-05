def solution():
  import sys
  input = sys.stdin.readline
  
  computerNum = int(input())
  computerNode = [False for _ in range(computerNum+1)]
  matrix = [[0 for _ in range(computerNum)] for _ in range(computerNum)]
  stack = [1]
  connectNum = int(input())
  for i in range(connectNum):
    [a, b] = list(map(int, input().split()))
    matrix[a-1][b-1] = 1; matrix[b-1][a-1] = 1
  while(len(stack) != 0):
    present = stack.pop()
    computerNode[present-1] = True
    for i in range(computerNum):
      if matrix[present-1][i] == 1 and computerNode[i] == False:
        stack.append(i+1)
  returnNum = 0
  for i in computerNode:
    if i == True: returnNum = returnNum + 1
  print(returnNum - 1)