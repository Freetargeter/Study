# 조건문에서 아무 일도 하게 않게 설정하고 싶다면?
pocket = ['paper','money','cellphone']
if 'money' in pocket:
  pass
else:
  print("카드를 꺼내라")
  
  
# if문을 한 줄로 작성하기
if 'money' in pocket:
  pass
else:
  print('카드를 꺼내라')
  
if 'money' in pocket: pass
else : print("카드를 꺼내라")

if score >= 60:
  message = 'success'
else:
  message = 'failurex'
  
message = 'success' if score >= 60 else 'failure'

