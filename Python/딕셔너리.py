a = {1:"hi"}
a = {'a':[1,2,3]}

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
print(a)

# 딕셔너리 요소 삭제하기
del a[1]
print(a)

# 딕셔너리를 만들 때 주의사항
a = {1:'a',1:'b'}
print(a)

# Key 리스트 만들기
a = {'name': 'pey','phone':'0119993323','birth':'1118'}
print(a.keys())

for k in a.keys():
  print(k)

print(list(a.keys()))

# Value 리스트 만들기
a.values()

# Key, Value 쌍 얻기
print(a.items())

# 쌍 모두 지우기
a.clear()
print(a)

# key로 value얻기
a = {'name': 'pey','phone':'0119993323','birth':'1118'}
a.get('name')
# => 존재하지 않는 키로 값을 가져오려 할 경우 a[1]은 오류를 발생시키고 a.get(1)은 None을 돌려준다는 차이가 있다.

a.get('foo','bar') # 키 값이 없을 경우 'bar'를 디폴트로 설정

# 해당 key가 딕셔너리 안에 있는지 조사하기
print('name' in a)




