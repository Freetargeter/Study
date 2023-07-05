def solution():
  import sys
  from collections import deque 
  
  input = sys.stdin.readline
  n, m, k, x = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  distance = [-1] * (n+1) 
  distance[x] = 0
  queue = deque([x])
  
  for _ in range(m):
    x1, x2 = map(int, input().split())
    graph[x1].append(x2)
    
  
  while queue:
    now = queue.popleft()
    for i in graph[now]:
      if distance[i] == -1:
        distance[i] = distance[now]+1
        queue.append(i)
  
  if k in distance:
    for i in range(1, n+1):
      if distance[i] == k:
        print(i)
  else: print(-1)
