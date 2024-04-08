# 파이프 옮기기 

# ver 1 : BFS로 접근하기 -> 시간 초과 
from collections import deque 
dr = [0, 1, 1]
dc = [1, 1, 0]

def bfs(r, c, d):
   global cnt 
   Q = deque()
   Q.append((r, c, d))

   while Q:
      cr, cc, cd = Q.popleft()
      # 기저 조건 
      if cr == cc == N - 1:
         cnt += 1
         continue

      s, e = 0, 0
      # 현재 위치, 방향 
      if cd == 0:       # 가로: 가로, 대각선
         s, e = 0, 2
      elif cd == 1:     # 대각선: 가로, 대각선, 세로
         s, e = 0, 3
      else:             # 세로: 대각선, 세로 
         s, e = 1, 3 

      for nd in range(s, e):
         nr = cr + dr[nd]
         nc = cc + dc[nd]
         # 벽이 긁히지 않게          
         if nr >= N or nc >= N: continue
         # 주변에 방해물이 있는지 
         if nd == 1:
            if home[cr + 1][cc] != 0 or  home[cr][cc + 1] != 0 or home[nr][nc] != 0:  continue
         else:
            if home[nr][nc] != 0:  continue 

         Q.append((nr, nc, nd))

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
bfs(0, 1, 0)
print(cnt)


















