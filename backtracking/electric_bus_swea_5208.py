
def func(idx, cnt, btr):
   global minV
   if cnt >= minV:
      return

   if idx == N:
      minV = min(minV, cnt)
      return
   
   if btr > 0:
      func(idx+1, cnt, btr-1)
   func(idx+1, cnt+1, arr[idx]-1)
   
for tc in range(1, int(input()) + 1):
   arr = list(map(int, input().split()))
   N = arr[0]
   arr = [0] + arr[1:]
   minV = N
   func(2, 0, arr[1]-1)
   print(f'#{tc} {minV}')



