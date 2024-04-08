# 선발명단 
def DFS(k, total):
   global maxV
   if k == 11:
      maxV = max(total, maxV)
   
   for i in range(0, 11):
      if not used[i]:
         if board[k][i]:
            used[i] = 1
            DFS(k + 1, total + board[k][i])
            used[i] = 0

for _ in range(int(input())):
   board = [list(map(int, input().split())) for _ in range(11)]
   used = [0] * 11
   maxV = 0
   DFS(0, 0)
   print(maxV)




