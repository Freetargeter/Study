# 정수형 int type
a = 123
print(type(a))

# 실수형 float type
a = 1.2
print(type(a))

a = 4.24e-10 # 4.24*10^-10, E와 e중 아무거나 사용해도 상관없음
print(type(a))

a = 4.24E10 # 4.24*10^10, E와 e중 아무거나 사용해도 상관없음
print(type(a))

# 8진수 0o또는 0O로 시작
a = 0o177 
print(a)

# 16진수 0x또는 0X로 시작
a = 0x8ff
print(a)

# 문자열 만드는 방법
# 1. 큰 따옴표로 양쪽 둘러싸기
# 2. 작은 따옴표로 양쪽 둘러싸기
# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""
# 3. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''

# 문자열에 작은 따옴표 포함시키기
# => 문자열을 큰따옴표로 둘러싸야 한다. 작은따옴표는 불가하다
food = "Python's favorite food is perl"

# 문자열에 큰따옴표 포함시키기
#  => 문자열을 작은 따옴표로 둘러싸야한다. 큰따옴표는 불가하다.
say =  '"Python is very easy." he says.'

# 백슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say =  "\"Python is very easy\" he says."

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1. 줄을 바꾸는 이스케이프 코드 삽입하기
multiline = "Life is too short\nYou need python"
# 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
multiline = '''
Life is too short
You need python
'''
multiline = """Life is too short
You need python"""

# 문자열 연산하기
# 1. 문자열 더해서 연결하기
head = "Python"
tail = "is fun!"
print(head + tail)

# 2. 문자열 곱하기
a = 'python'
print(a * 2)

# 3. 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])
print(a[-1])

# 문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[:])
print(a[1:-1])

# 문자열 포맷팅
# 1. 숫자 바로 대입
print("I eat %d apples"%3)
print("I eat %d apples" % 3)

# 2. 문자열 바로 대입
print("I eat %s apples."% "five")

# 3. 숫자 값을 나타내는 변수로 대입
num = 6
print("I eat %d apple"%num)

# 4. 2개 이상의 값 넣기
num =10
day = "three"
print("I ate %d apples. so I was sick for %s days" %(num,day))

# %s : 문자열
# %c : 문자 1개
# %d : 정수
# %f : 부동 소수
# %o : 8진수
# %x : 16진수
# %% : Literal %


# 포맷코드와 숫자 함께 사용하기

# 1. 정렬과 공백
print("%10s"%"hi")




