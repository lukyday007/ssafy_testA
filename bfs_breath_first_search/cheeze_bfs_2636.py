# 바깥 공간 기준 
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
   Q = deque()
   Q.append((r, c))

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]



# Q = deque()
# traverse = 2
# while traverse < 5 and Q:
#    for r in range(R):
#       for c in range(C):
#          if board[r][c] == 0 and visited[r][c] == 0:
#             visited[r][c] = 1
#             for d in range(4):
#                nr = r + dr[d]
#                nc = c + dc[d]
#                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
#                if board[nr][nc] == 1 and visited[nr][nc] == 0:
#                   visited[nr][nc] = traverse

#    traverse += 1
#    print()
#    print()
#    for v in visited:
#       print(*v)













