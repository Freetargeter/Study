def solution():
  import sys
  input = sys.stdin.readline
  
  n = int(input())
  sanggeun_cards = list(map(int, input().split()))
  m = int(input())
  discrimanate_cards = list(map(int, input().split()))
  
  sanggeun_cards.sort()
  
  
  def isNumIncluded(num):
    l_id = 0
    r_id = len(sanggeun_cards)-1
    while(r_id - l_id >= 0):
      m_id = (l_id + r_id) // 2
      if sanggeun_cards[m_id] > num:
        r_id = m_id-1
      elif sanggeun_cards[m_id] < num:
        l_id = m_id+1
      else:
        return m_id
    return None
    
    
  for i in discrimanate_cards:
    if isNumIncluded(i) is not None:
      print(1, end=" ")
    else:
      print(0, end=" ")