# 오류 발생
# 1.  f  = open("나없는파일",'r')
# 2.  4 / 0
# 3.  a = [1,2,3];  a[4]

# 오류 예외 처리 기법

# try, except문
try:
  ...
except[발생 오류[as 오류 메시지 변수]:
  ...
  
# 1. try,, except만 쓰는 방법
try:
  ...
except:
  ...
# 2. 발생 오류만 포함한 except문
try:
  ...
except 발생 오류:
  ...
# 3. 발생 오류와 오류 메시지 변수까지 포함한 except문
try:
  ...
except 발생 오류 as 오류 메시지 변수:
  ...
  
# EX)
try:
  4 / 0
except ZeroDivisionError as e:
  print(e)
# 결과값: division by zero

# EX2)
try:
  4 / 0
except ZeroDivisionError as e:
  print("0으로 나눌 수 없습니다")
except ZeroDivisionError as e:
  print("인덱싱할 수 없습니다")
  
# 오류 회피하기
try:
  f = open("나없는파일",'r')
except FileNotFoundError:
  pass
  
# 오류 일부러 발생시키기 raise 이용
class Bird:
  def fly(self):
    raise NotImplementedError
# NotImplementedError: 상속받는 자식 클래스가 fly함수를 구현하지 않으면 오류발생

class Eagle(Bird):
  pass
  
eagle = Eagle()
eagle.fly() # => 오류발생

class Eagle(Bird):
  def fly(self):
    print("very fast")
  
eagle = Eagle()
eagle.fly() # => 정상작동

# 예외 만들기
class MyError(Exception):
  pass
  
def say_nick(nick):
  if nick == '바보':
    raise MyError()
  print(nick)
  
try:
  say_nick("천사")
  say_nick("바보")
except MyError as e:
  print("허용되지 않는 별명입니다.")
  print(e)
  
  ## 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면 오류 클래스에 다음과 같은 __str__메서드를 구현해야 한다
  

class MyError(Exception):
  def __str__(self):
    return "허용되지 않는 별명입니다."