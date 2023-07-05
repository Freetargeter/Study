def solution():
  n, m = map(int, input().split())
  s = []
  def dfs(k):
    if len(s)==m:
      print(' '.join(map(str,s)))
    
    for i in range(k, n+1):
      if i not in s:
        s.append(i)
        dfs(i+1)
        s.pop()
        
  dfs(1)