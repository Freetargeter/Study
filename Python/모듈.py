def add(a, b):
  return a + b

def sub(a, b):
  return a - b

# 직접 이 파일을 실행시킬 때만 if문 안의 문장이 수행되도록 함
if __name__ == "__main__":
  print(add(1,4))
  print(sub(4,2))

# >>> import 모듈
# >>> print(모듈.add(3,4))

# >>> from 모듈 import add
# >>> add(3,4)

# >>> from 모듈 import add, sub
# >>> from 모듈 import *


# 클래스나 변수 등을 포함한 모듈
PI = 3.141592

class Math:
  def solv(self, r):
    return PI * (r ** 2)

def add(a, b):
  return a+b

