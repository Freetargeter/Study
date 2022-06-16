# 리스트 더하기

a = [1,2,3]
b = [4,5,6]
print(a+b)

# 리스트 반복하기
print(a*3)

# 리스트 길이 구하기
print(len(a))

# 리스트 값 수정하기
a = [1,2,3]
a[2] = 4

# del 함수 사용해 리스트 요소 삭제하기
del a[1]
print(a)
del a[2:]

# 리스트에 요소 추가
a.append(4)
a.append([4,5])

# 리스트 정렬
a = [1,2,3,1]
a.sort()
print(a)

a = ['a','d','c']
a.sort()
print(a)

a.reverse()
print(a)

# 위치 반환
a = [1,2,3]
print(a.index(3))

# 요소 삽입
a = [1,2,3]
a.insert(0,4) # 0번째 위치에 4삽입

# 리스트 요소 제거
a = [1,2,3,1,2,3]
a.remove(3) # 첫번째로 나오는 3제거
print(a)

# 리스트 요소 끄집어내기
a.pop()
print(a)

# 리스트에 포함된 요소 x의 개수 세기
a = [1,2,3,1]
print(a.count(1))

# 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)

