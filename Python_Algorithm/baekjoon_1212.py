def convertToBinaryList(num):
  
  binary = ""
  numList = [4, 2, 1]
  
  for i in numList:
    if num >= i:
      binary = binary + "1"
      num = num - i
    else: binary = binary + "0"  
    
  return binary
  
def solution():
  
  import sys
  input = sys.stdin.readline
  print(bin(int(input(), 8))[2:])
  # octal = input()
  # binary = ""

  # for i in range(len(octal)):
  #   num = int(octal[i])
  #   numList = [4, 2, 1]

  #   for i in numList:
  #     if num >= i:
  #       binary = binary + "1"
  #       num = num - i
  #     else: binary = binary + "0"  
    
  # print(int(binary))
    
      
    