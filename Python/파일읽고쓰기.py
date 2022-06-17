# f = open("새파일.txt",'w')
# f.close()

# # 파일 생성
# # 파일 객체 = open(파일 이름, 파일 열기 모드)

# # r: 읽기 모드 - 파일을 읽기만 할 때 사용
# # w: 쓰기 모드 - 파일에 내용을 쓸 때 사용
# # a: 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용

# f = open("User/study/새파일.txt",'w')

# # 파일을 쓰기 모드로 열어 출력값 적기
# f = open('새파일.txt','w')
# for i in range(1, 11):
#   data = "%d번째 줄입니다\n"%i
#   f.write(data)
# f.close()

# # 프로그램 외부에 저장된 파일을 읽는 여러가지 방법

# # readline함수 사용하기
# f = open("User/study/새파일.txt",'r')
# line = f.readline()
# print(line)
# f.close()

# # 모든 줄을 읽고 싶을 때
# f = open("User/study/새파일.txt",'r')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line)
# f.close()

# # readlines 사용하기 # 모든 줄을 요소로 갖는 리스트로 돌려준다.
# f = open("User/study/새파일.txt",'r')
# lines = f.readlines()
# for lines in lines:
#   print(line)
# f.close()


# # read 함수 사용하기
# f = open("User/study/새파일.txt",'r')
# data = f.read()
# print(data)
# f.close()

# # 파일에 새로운 내용 추가하기
# f = open("User/study/새파일.txt",'a')
# for i in range(11,20):
#   data = "%d번째 줄입니다\n"%i
#   f.write()
# f.close()

# # with문과 함께 살펴보기
# f = open("User/study/새파일.txt",'w')
# f.write("Life is too short, you need python")
# f.close()

# with open('foo.txt','w') as f:
#   f.write("Life is too short, you need python")
  
# sys 모듈로 매개변수 주기
import sys

args = sys.argv[1:]
for i in args:
  print(i)


