
  
  
def solution():
  import sys
  input = sys.stdin.readline
  N, M = map(int, input().split())
  cards = list(map(int, input().split()))
  cards = sorted(cards)
  result = 0
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        if cards[i] + cards[j] + cards[k] > M:
          continue
        else:
          result = max(result, cards[i] + cards[j] + cards[k])
  print(result)
  
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# N, M = map(int, input().split(' '))
# sum = list(map(int, input().split(' ')))

# sum_list = combinations(sum, 3)
# result = 0
# for x, y, z in sum_list:
#     r = x+y+z
#     if r <= M and result < r:
#         result = r

# print(result)