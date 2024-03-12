# 3 차원 배열과 델타 
from collections import deque
dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(visited, riped_tomatoes, warehouse):
   Q = deque()
   for r, c, z in riped_tomatoes:
      Q.append((r, c , z))
      visited[z][r][c] = 1

   move = 0
   while Q:
      r, c, z = Q.popleft()
      for d in range(6):
         nr = r + dr[d]
         nc = c + dc[d]
         nz = z + dz[d]
         if nr < 0 or nr >= R or nc < 0 or nc >= C or nz < 0 or nz >= Z: continue
         if visited[nz][nr][nc] == 0 and warehouse[nz][nr][nc] == 0:
            Q.append((nr, nc, nz))
            visited[nz][nr][nc] = visited[z][r][c] + 1
            move = visited[nz][nr][nc] - 1

   for visit in visited:
      for v in visit:
         if 0 in v:
            return -1
         
   return move 

def get_answer(R, C, Z):
   warehouse = [[list(map(int, input().split())) for _ in range(R)] for _ in range(Z)]

   # 덜익은 토마토가 없는 상태 
   ripe = False
   riped_tomatoes = []
   no_tomato = []
   for c in range(C):
      for r in range(R):
         for z in range(Z):
            # 덜 익은 토마토가 있으면 True
            if warehouse[z][r][c] == 0:
               ripe = True
            # 익은 토마토 좌표 놓기 -> BFS 사용
            elif warehouse[z][r][c] == 1:
               riped_tomatoes.append((r, c, z))
            # 토마토 없는 좌표 -> visited 에 넣기 
            elif warehouse[z][r][c] == -1:
               no_tomato.append((r, c, z))

   # 덜익은 토마토가 없으면 계속 False -> 0 출력 
   if not ripe:
      print(0)
      return
   
   # 토마토가 모두 익지 못하는 상황이면 -1 출력
   visited = [[[0] * C for _ in range(R)] for _ in range(Z)]
   for r, c, z in no_tomato:
      visited[z][r][c] = -1

   print(bfs(visited, riped_tomatoes, warehouse))

C, R, Z = map(int, input().split())
get_answer(R, C, Z)















