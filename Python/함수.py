# 입력값이 없는 함수
def say():
  return 'Hi'

a = say()
print(a)

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args):
  result = 0
  for i in args:
    result = result + i
  return result

def add_mul(choice, *args):
  if choice == 'add':
    result = 0
    for i in args:
      result = result + i
  elif choice == 'mul':
    result = 1
    for i in args:
      result = result * i
  return result

# 함수 안에서 함수 밖의 변수를 변경하는 방법

# 1. return 사용하기
a  = 1
def vartest(a):
  a = a + 1
  return 1

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest():
  global a
  a = a + 1
  
vartest()
print(a)

# lambda : 함수를 한 줄로 간결하게 만들 때 사용
add = lambda a, b: a+b
result = add(3,4)
print(result)

