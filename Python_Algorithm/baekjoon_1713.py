def solution():
  import sys
  input = sys.stdin.readline
  
  n = int(input())
  total_cnt = int(input())
  recommend_in_turn = list(map(int, input().split()))
  
  cand = []
  recm = []
  
  def findPoorCand():
    lowest_num = 1001
    min_id = -1
    for i, v in enumerate(recm):
      if v < lowest_num:
        lowest_num = v
        min_id = i
    return min_id
  
  for i, v in enumerate(recommend_in_turn):
    if v in cand:
      id = cand.index(v)
      recm[id] += 1
    else:
      if len(cand) >= n:
        min_id = findPoorCand()
        del cand[min_id]
        del recm[min_id]
      cand.append(v)
      recm.append(0)
        
  for i in sorted(cand):
    print(i)
        
      
        
        
      
  
        