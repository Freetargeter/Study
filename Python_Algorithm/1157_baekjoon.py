word = input()
dic = dict()

for i in word:
  o = ord(i)
  i = i.upper()
  if i in dic.keys():
    dic[i] = dic[i] + 1
  else:
    dic[i] = 1
      
print(dic)
      
max = 0
result = ""

for i in dic.keys():
  if dic[i] > max:
    max = dic[i]
    result = i
  elif dic[i] == max:
    result = "?"

print(result)