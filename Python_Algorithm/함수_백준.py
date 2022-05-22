
# def solve(a:list) :
#   sum = 0
#   for i in range(len(a)):
#     sum = sum + a[i]
#   return sum


# def solve():
#   li = list(range(10000))
#   print(li)
#   for i in range(10000): 
#     d = makeD(i)
#     if d in li:
#       li.remove(d)
#   for i in range(len(li)):
#     print(li[i])
    
# def makeD(num):
#   a = num
#   c = num
#   leng = len(str(num))
#   for i in range(leng):
#     a = a + num // 10**(leng-i-1)
#     num = num - (10**(leng-i-1))*(num // 10**(leng-i-1))
#   return a

# solve()

# def solve():
#   a = -1
#   for i in range(10000):
#     if a < 8 :
#       a = a + 2
#     else :
#       a = a + 11
#       if a > 10000:
#         break
#     print(a)
# solve()


def solve(a):
  li  = makeH()
  rv = 0
  for i in range(len(li)):
    if li[i] < a:
      rv = rv +1
    else:
      return rv
    
def makeH():
  li = list()
  for i in range(1,1000,1):
    nLi = list(map(int,str(i)))
    if len(nLi)==1:
      li.append(i)
    elif len(nLi)==2:
      li.append(i)
    else :
      if nLi[2] + nLi[0] == nLi[1]*2 and nLi[2] <= nLi[0]:
        li.append(i)
  return li
        
a = int(input())      
        
print(solve(a))