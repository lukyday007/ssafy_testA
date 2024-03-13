# # 바깥 공간 기준 
# from collections import deque
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def bfs(points, traverse):
#    Q = deque()
#    for r, c in points:
#       if visited[r][c] == 0:
#          visited[r][c] = traverse

# R, C = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(R)]
# visited = [[0] * C for _ in range(R)]

# for r in range(R):
#    for c in range(C):
#       if board[r][c] == 0 and visited[r][c] == 0:
#          visited[r][c] = 1

# print()
# for v in visited:
#    print(*v)

# edge = []
# traverse = 2
# # while any(0 in v for v in visited):
# # while traverse < 3:
# for r in range(R):
#    for c in range(C):
#       if board[r][c] == 0 and visited[r][c] != 0:
#          for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
#             if board[nr][nc] == 1 and visited[nr][nc] == 0:
#                edge.append((nr, nc))
#                visited[nr][nc] = traverse
               
# # for e in edge:
# #    print(*e)
#    # print()
#    # bfs(edge, traverse)
#    # traverse += 1
#    # print(len(edge))
   
#    # for cc, cr in edge:
#    #    if visited[cc][cr] == traverse - 1:
#    #       board[cc][cr] = 0
#    # edge = []

#    # print('board')
#    # for b in board:
#    #    print(*b)

# print()
# print('visited')
# for v in visited:
#    print(*v)


# from collections import deque
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# R, C = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(R)]
# visited = [[0] * C for _ in range(R)]

# def bfs():
#    air = deque()
#    newAir = deque()
#    visited[0][0] = 1
#    air.append((0, 0))
#    hour = 0

#    while air:
#       r, c = air.popleft()
#       for d in range(4):
#          nr = r + dr[d]
#          nc = c + dc[d]
#          if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
#          # 방문처리 
#          visited[nr][nc] = 1
#          # 공기면 air. append 계속 탐색 
#          if board[nr][nc] == 0:
#             air.append((nr, nc))
#          # 치즈면 newAir.append 저장
#          else:
#             newAir.append((nr, nc))
      
#       if not newAir:
#          break
      
#       hour += 1
#       print(air)
#       print(newAir)
#       air, newAir = newAir, air

#    print(hour)
#    print(air)

# bfs()


from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
   air = deque()
   new_air = deque()
   visited[0][0] = 1
   air.append((0, 0))
   hour = 0
   left_cheeze = 0

   while True:
      while air:
         r, c = air.popleft()
         for d in range(4):
               nr = r + dr[d]
               nc = c + dc[d]
               if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                  visited[nr][nc] = 1
                  if board[nr][nc] == 0:
                     air.append((nr, nc))
                  else:
                     new_air.append((nr, nc))

      if len(new_air) == 0:
         break   
      else:
         hour += 1
         left_cheeze = len(new_air)
         air, new_air = new_air, air

   print(hour)
   print(left_cheeze)

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
bfs()


















