
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

# 2. 소수점 표현하기
print("%0.4f"%3.421345234)
print("%10.4f"%3.421345234)

# format 함수를 사용한 포매팅

# - 숫자 바로 대입하기
print("I eat {0} apples.".format(3))

# - 문자열 바로 대입하기
print("I eat {0} apples.".format("five"))

# - 숫자 값을 가진 변수로 대입하기
num = 3
print("I eat {0} apples.".format(num))

# - 2개 이상의 값 넣기
day ="three"
print("I eat {0} apples. so I was sick for {1} days".format(num,day))

# - 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days".format(number=10,day=3))

# - 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days".format(10,day=3))
# => 인덱스가 먼저 나올 수는 있지만 이름이 먼저 나오면 인덱스는 뒤에서 못나온다.

# - 왼쪽 정렬 (문자열의 총자릿수를 10으로 맞춤)
print("{0:<10}hi".format("hi"))

# - 오른쪽 정렬 
print("{0:>10}".format("hi"))

# - 가운데 정렬
print("{0:^10}".format("hi"))

# - 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# - 소수점 표현하기
y = 3.421542345
print("{0:.4f}".format(y))
print("{0:>10.4f}".format(y))

# - {}문자 표현하기
print("{{ and }}".format())


# - f 문자열 포매팅
name = "홍길동"
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
print(f"나는 내년이면 {age+1}살이 된다.")
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다.')
print(f'{"hi":>10}')

# 문자열 관련 함수

a = 'hobby'
print(a.count('b'))

a = 'Python is the best choice'
print(a.find('b'))

a = "Life is too short"
print(a.index("t")) # find와 다르게 문자열이 포함되지 않으면 오류를 발생시킴 find는 -1을 반환

print(",".join("abcd"))

print(",".join(['a','b','c','d']))

# - 소문자, 대문자로 바꾸기
a = "HI"
print(a.lower())
a = 'hi'
print(a.upper())

# - 왼쪽, 오른쪽, 양쪽 공백 지우기
a = ' hi '
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# - 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life","Your leg"))

# - 문자열 나누기
a = "Life is too short"
print(a.split())
b = 'a:b:c:d'
print(b.split(":"))


