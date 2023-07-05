def solution():
  n, m = map(int, input().split())
  nums = list(map(int, input().split()))
  nums.sort()
  s = []
  def dfs():
    if len(s) == m:
      print(' '.join(map(str, [nums[j] for j in s])))
      return
    for i in range(n):
      s.append(i)
      dfs()
      s.pop()
  dfs()