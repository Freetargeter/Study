import sys

N, M = map(int,sys.stdin.readline().split())
PD = list()
RI = list()

for i in range(N):
  PKM = sys.stdin.readline()
  PD.append(PKM)
# print(PD)
for i in range(M):
  IP = input()
  # print(IP)
  if type(IP) == 'int':
    RI.append(PD[IP])
  elif type(IP) == 'str':
    RI.append(PD.index(IP))
# print(RI)    
for i in RI:
  print(RI[i])