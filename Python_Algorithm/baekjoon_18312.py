def solution():
  N, K = map(int, input().split())
  time = [0,0,0,0,0,0]
  count = 0
  for _ in range(3600*(N+1)):
    if K in time: count += 1
    time[5] += 1
    if time[5] == 10: time[5] = 0; time[4] += 1
    if time[4] == 6:  time[4] = 0; time[3] += 1
    if time[3] == 10: time[3] = 0; time[2] += 1
    if time[2] == 6:  time[2] = 0; time[1] += 1
    if time[1] == 10: time[1] = 0; time[0] += 1
  print(count)
  