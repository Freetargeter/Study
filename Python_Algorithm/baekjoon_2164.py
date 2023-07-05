def solution():
  
  N = int(input())
  
  arr = [i for i in range(1,N+1)]
  boolean = False
  
  while True:
    if len(arr) == 1:
      print(arr[0])
      break
    
    newArr = []
    
    for i in arr:
      if boolean:
        newArr.append(i)
      boolean = not boolean
    
    arr = newArr
    
          


