# 연구소 
from collections import deque
import copy
# 세울 수 있는 벽이 3개 = 깊이가 3인 DFS
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS(Q):
   cnt = 0

   while Q:
      cr, cc = Q.popleft()
      for d in range(4):
         nr = cr + dr[d]
         nc = cc + dc[d]
         if 0 <= nr < N and 0 <= nc < M:
            if labo[nr][nc] == 0:
               labo[nr][nc] = 2
               cnt += 1
   
   labo = oriLabo    # 초기화
   return cnt
            

def DFS(k, r, c):
   global maxV, wall

   if k == 3:
      result = BFS(virus) # 퍼진 바이러스의 총 개수
      res = M * N - (result + virus_cnt) - wall - 3
      if maxV > res:
         return
      maxV = max(res, maxV)
      return 
   
   for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]
      if 0 <= nr < N and 0 <= nc < M:
         if labo[nr][nc] == 0:
            labo[nr][nc] = 1
            DFS(k + 1, nr, nc)
            labo[nr][nc] = 1
         

N, M = map(int, input().split())
labo = [list(map(int, input().split())) for _ in range(N)]
oriLabo = copy.deepcopy(labo) # 초기화용 
wall = 0
maxV = 0

virus = deque()
for n in range(N):
   for m in range(M):
      if labo[n][m] == 2:
         virus.append((n, m))
      elif labo[n][m] == 1:
         wall += 1

virus_cnt = len(virus)
for r in range(N):
   for c in range(M):
      if labo[r][c] == 1:
         DFS(0, r, c)
         break














