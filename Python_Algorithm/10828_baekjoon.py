import sys

NOO = int(input())
stack = list()

for i in range(NOO):
  order = sys.stdin.readline().split()
  RO = order[0]
  if RO == 'push':
    stack.append(order[1])
  elif RO == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif RO == 'size':
    print(len(stack))
  elif RO == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif RO == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[len(stack)-1])