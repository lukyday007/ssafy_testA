# 적록색약
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def bfs(r, c, visited, cha):
    Q = deque()
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc] == 0 and board[nr][nc] == cha:
                visited[nr][nc] = 1
                Q.append((nr, nc))
    return

N = int(input())
board = [list(input()) for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
xblind = 0
for r in range(N):
    for c in range(N):
        if visited1[r][c] == 0:
            bfs(r, c, visited1, board[r][c])
            xblind += 1

for r in range(N):
    for c in range(N):
        if board[r][c] == "R":
            board[r][c] = "G"
blind = 0
for r in range(N):
    for c in range(N):
        if visited2[r][c] == 0:
            bfs(r, c, visited2, board[r][c])
            blind += 1

print(xblind, blind)
'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def bfs(r, c, visited, cha):
    Q = deque()
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc] == 0 and board[nr][nc] == cha:
                visited[nr][nc] = 1
                Q.append((nr, nc))
    return

N = int(input())
board = [list(input()) for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
xblind = 0
for r in range(N):
    for c in range(N):
        if visited1[r][c] == 0:
            bfs(r, c, visited1, board[r][c])
            xblind += 1

for r in range(N):
    for c in range(N):
        if board[r][c] == "R":
            board[r][c] = "G"
blind = 0
for r in range(N):
    for c in range(N):
        if visited2[r][c] == 0:
            bfs(r, c, visited2, board[r][c])
            blind += 1

print(xblind, blind)
