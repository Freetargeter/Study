def solution():
  n = int(input())
  start, end = 0, 2**32
  answer = -1
  while start <= end:
      mid = (start + end) // 2
      if mid ** 2 > n:
          end = mid - 1
      elif mid ** 2 < n:
          start = mid + 1
      else:
          answer = mid
          break

  if answer == -1: answer = end+1 
  print(answer)