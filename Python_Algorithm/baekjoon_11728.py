def problem_11728():
  import sys
  input = sys.stdin.readline
  [n, m] = list(map(int,input().split()))
  a = list(map(int,input().split())); b = list(map(int,input().split()))
  al = []
  ai = 0; bi = 0

  while(True):
    if len(a) == ai and len(b) == bi: break
    if len(a) != ai and len(b) != bi:
      if a[ai] <= b[bi]:
        al.append(a[ai])
        ai+=1
      else:
        al.append(b[bi])
        bi+=1
    elif len(a) != ai:
      al.extend(a[ai:])
      break
    else: 
      al.extend(b[bi:])
      break

  for i in al:
    print(i, end=" ")
