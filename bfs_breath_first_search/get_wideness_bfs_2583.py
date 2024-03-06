from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# def bfs(r, c, cnt):
#     Q = deque()
#     Q.append((r, c))
#     visited[r][c] = 1

#     while Q:
#         r, c = Q.popleft()
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if 0 <= nc < N and 0 <= nr < M and visited[nr][nc] == 0 and board[nr][nc] == 0:
#                 visited[nr][nc] = 1
#                 Q.append((nr, nc))
#                 cnt += 1
#     return cnt

# M, N, K = map(int, input().split())
# board = [[0] * N for _ in range(M)]
# visited = [[0] * N for _ in range(M)]
# for _ in range(K):
#     a, b, c, d = map(int, input().split())
#     for i in range(a, c):
#         for j in range(b, d):
#             board[j][i] = 1

# print(len(board))
# print(len(board[1]))
# for b in board:
#     print(*b)

# ans = []
# for r in range(M):
#     for c in range(N):
#         if board[r][c] == 0 and visited[r][c] == 0:
#             ans.append(bfs(r, c, 1))
# print(ans)


def bfs(y, x, cnt):
    Q = deque()
    Q.append((y, x))
    visited[y][x] = 1

    while Q:
        ny, nx = Q.popleft()
        for d in range(4):
            nr = ny + dr[d]
            nc = nx + dc[d]
            if 0 <= nr < y and 0 <= nc < x and visited[nr][nc] == 0 and board[nr][nc] == 0:
                cnt += 1
                Q.append((nr, nc))
                visited[nr][nc] = 1
        
    return cnt

x, y, k = map(int, input().split())
board = [[0] * x for _ in range(y)]
visited = [[0] * x for _ in range(y)]
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for ny in range(y1, y2):
        for nx in range(x1, x2):
            board[ny][nx] = 1

for b in board:
    print(*b)

res = []
for ny in range(y):
    for nx in range(x):
        if board[ny][nx] == 0 and visited[ny][nx] == 0:
            res.append(bfs(ny, nx, 1))
            
print(res)






