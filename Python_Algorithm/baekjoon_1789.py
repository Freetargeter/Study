def solution():
  n = int(input())
  l_num = 1
  r_num = n
  
  while(r_num - l_num > 1):
    middle_num = int((l_num + r_num) / 2)
    account = (middle_num**2 + middle_num) / 2
    if account > n:
      r_num = middle_num
    elif account < n:
      l_num = middle_num
    else:
      l_num = middle_num
      break
  print(l_num)