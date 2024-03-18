# 미로 탐색 
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
   pass
   Q = deque()
   Q. append((0, 0))
   visited[0][0] = 1

   while Q:
      r, c = Q.popleft()
      for d in range(4):
         nr = r + dr[d]
         nc = c + dc[d]
         if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and maze[nr][nc] == "1":
            Q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs()
print(visited[N-1][M-1])





