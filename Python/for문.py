# 리스트 내포 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
  result.append(a*3)
  
result = [num * 3 for num in a]

result = [num * 3 for num in a if num % 2 == 0]

result = [x*y for x in range(2, 10)
          for y in range(1, 10)]

