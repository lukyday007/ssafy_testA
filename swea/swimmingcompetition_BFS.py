from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
sr, sc = map(int, input().split())
er, ec = map(int, input().split())
answer = N ** 2 # 수영장의 크기 ^ 2

Q = deque()
Q.append((sr, sc, 0))
while Q:
   cr, cc, time = Q.popleft()
   visit[cr][cc] = True

   if cr == er and cc == ec:
      answer = min(answer, time)
      continue

   for d in range(4):
      nr, nc = cr + dr[d], cc + dc[d]

      if 0 <= nr < N and 0 <= nc < N:
         # 장애물이 있으면 피하기
         if sea[nr][nc] == 1:
            continue 
         # 방문하지 않으면 
         if not visit[nr][nc]:
            next_time = time
            # 소용돌이가 있고 아직 넘을 수 없는 시간일 때 
            if sea[nr][nc] == 2 and (time - 2) % 3 != 0:
               while (next_time - 2) % 3 != 0:
                  # 넘을 수 있는 시간까지 계속 더함 
                  next_time += 1
                  print(f'next_time: {next_time}')

            Q.append((nr, nc, next_time + 1))

print(answer)


# from collections import deque

# directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# N = int(input())
# board = []
# for _ in range(N):
#    board.append(list(map(int, input().split())))

# visited = [[False for _ in range(N)] for _ in range(N)]
# answer = N ** 2
# A, B = map(int, input().split())
# C, D = map(int, input().split())

# dq = deque([(A, B, 0)])
# while dq:
#    y, x, now = dq.popleft()
#    visited[y][x] = True
#    if (y, x) == (C, D):
#       answer = min(answer, now)
#       continue

#    for dy, dx in directions:
#       nx, ny = x + dx, y + dy
#       if 0 <= nx < N and 0 <= ny < N:
#          if board[ny][nx] == 1:
#             continue
#          if not visited[ny][nx]:
#             next_time = now
#             if board[ny][nx] == 2 and (now - 2) % 3 != 0:
#                while (next_time - 2) % 3 != 0:
#                      next_time += 1
#             dq.append((ny, nx, next_time + 1))

# if answer == N ** 2:
#    answer = -1

# print(answer)
