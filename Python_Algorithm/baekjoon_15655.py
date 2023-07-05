def solution():
  n, m = map(int,input().split())
  nums = list(map(int, input().split()))
  nums.sort()
  s = []
  def dfs(k):
    if len(s) == m:
      print(' '.join(map(str,[nums[j] for j in s])))
    
    for i in range(k, n):
      if i not in s:
        s.append(i)
        dfs(i+1)
        s.pop()
  dfs(0)