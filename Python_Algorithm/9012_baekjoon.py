from sys import stdin

n = int(stdin.readline())
for i in range(n):
  string = str(stdin.readline())
  stack = []
  for k in range(len(string)):
    if string[k] == '(':
      stack.append('(')
    elif string[k] == ')':
      if len(stack) == 0 or stack.pop() != '(': 
        print('NO')
        break
    if k == len(string)-1:
      if len(stack) == 0:
        print('YES')
      else:
        print('NO')  
        
  
