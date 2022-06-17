a = [1,2,3]
print(id(a))

b = a # a를 수정하면 b에 반영되고 b를 수정하면 a에 반영된다
print(id(a))
print(id(b))

b.append(34)

print(id(a))
print(id(b))

print(a is b)
print(a == b)

# a를 복사하면서 a와 b의 주소가 다르게 만들기
# 1. [:]사용
b = a[:]

# 2. copy 모듈 사용
from copy import copy
b = copy(a)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life' # 위의 방법과 동일

[a, b] = ['python', 'life']

a = b = 'python'

a, b = b, a # 두 변수의 값 바꾸기



