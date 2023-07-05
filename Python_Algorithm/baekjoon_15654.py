def solution():
  n, m = map(int, input().split())
  nums = list(map(int, input().split()))
  nums.sort()
  s = []
  def nums_print(s):
    print(' '.join(map(str,[nums[j] for j in s])))
  def dfs():
    if len(s) == m:
      nums_print(s)
    for i in range(n):
      if i not in s:
        s.append(i)
        dfs()
        s.pop()
        
  dfs()
      