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
