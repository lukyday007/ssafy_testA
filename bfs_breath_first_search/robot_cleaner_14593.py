# ver 1 
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# def check(r, c):
#    if 0 <= r < N and 0 <= c < M:
#       return True
#    return False 

# def possible(r, c):
#    for d in range(4):
#       nr = r + dr[d]
#       nc = c + dc[d]
#       if check(nr, nc):
#          if room[nr][nc] == 0 and visit[nr][nc] == False:
#             return True
#    return False 

# def dfs(r, c, d):
#    global clean
#    # st = [(r, c, d)]
#    # 청소 
#    if visit[r][c] == 0:
#       visit[r][c] = True
#       clean += 1
#       print(clean)
      
#    # 4 방향 중 청소 X
#    if not possible(r, c):          
#       # 후진 방향 set
#       nd = (d + 2) % 4
#       # 범위 확인 
#       if check(r + dr[nd], c + dc[nd]):
#          # 뒤에 벽 때문에 후진 불가
#          if room[r + dr[nd]][c + dc[nd]] == 1: 
#             return 
#          # 후진 가능 
#          else: 
#             return dfs(r + dr[nd], c + dc[nd], d)
                
#    else:    # 청소할 곳 있음
#       flag = True
#       nr, nc = 0, 0
#       while flag:
#          nd = (d - 1) % 4  # 반시계 방향 전환 
#          if check(r + dr[nd], c + dc[nd]):   # 범위 체크 
#             nr = r + dr[nd]
#             nc = c + dc[nd]
#             if room[nr][nc] == 0 and not visit[nr][nc]:
#                #     방향기준 앞 O -> 전진 -> 청소
#                return dfs(nr, nc, nd)
#                flag = False
                  
# N, M = map(int, input().split())
# R, C, D = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(N)]
# visit = [[False] * N for _ in range(M)]
# clean = 0

# dfs(R, C, D)
# print(clean)


# ver 2
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# def check(r, c):
#    if 0 <= r < N and 0 <= c < M:
#       return True
#    return False 

# def possible(r, c):
#    for d in range(4):
#       nr = r + dr[d]
#       nc = c + dc[d]
#       if check(nr, nc):
#          if room[nr][nc] == 0 and not visit[nr][nc]:
#                return True
#    return False 

# def dfs(r, c, d):
#    global clean
#    stack = [(r, c, d)]
#    while stack:
#       r, c, d = stack.pop()
#       # 청소 
#       if not visit[r][c]:
#          visit[r][c] = True
#          clean += 1
#       # 4 방향 중 청소 X
#       if not possible(r, c):
#          # 후진 방향 set
#          nd = (d + 2) % 4
#          # 범위 확인 
#          if check(r + dr[nd], c + dc[nd]):
#                # 뒤에 벽 때문에 후진 불가
#                if room[r + dr[nd]][c + dc[nd]] == 1: 
#                   return 
#                # 후진 가능 
#                else: 
#                   stack.append((r + dr[nd], c + dc[nd], d))          
#       else:    # 청소할 곳 있음
#          flag = True
#          nr, nc = 0, 0
#          while flag:
#                nd = (d - 1) % 4  # 반시계 방향 전환 
#                if check(r + dr[nd], c + dc[nd]):   # 범위 체크 
#                   nr = r + dr[nd]
#                   nc = c + dc[nd]
#                   if room[nr][nc] == 0 and not visit[nr][nc]:
#                      # 방향기준 앞 O -> 전진 -> 청소
#                      stack.append((nr, nc, nd))
#                      flag = False
#    return clean

# N, M = map(int, input().split())
# R, C, D = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(N)]
# visit = [[False] * M for _ in range(N)]
# clean = 0

# result = dfs(R, C, D)
# print(clean)


# ver 3
# 어차피 방의 끝은 1로 감싸져 있음
#  -> 범위 설정할 필요 없음!
dr = [-1, 0, 1, 0]  # 상우하좌
dc = [0, 1, 0, -1]

def possible(r, c):
   for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]
      if room[nr][nc] == 0:
         return True
   return False

def dfs(r, c, d):
   global clean

   # 청소
   if room[r][c] == 0:
      # 방문 체크 대신, 0 -> 2로 체크 
      room[r][c] = 2
      clean += 1

   if not possible(r, c):  # 4 방향 중 청소 X
      # 후진 방향 set
      nd = (d + 2) % 4
      # 뒤에 벽 때문에 후진 불가
      if room[r + dr[nd]][c + dc[nd]] == 1:
         return False
      # 후진 가능
      else:
         return dfs(r + dr[nd], c + dc[nd], d)

   else:  # 청소할 곳 있음
      nr, nc = 0, 0
      for i in range(1, 5):
         nd = (d - i) % 4  # 반시계 방향 전환
         nr = r + dr[nd]
         nc = c + dc[nd]

         if room[nr][nc] == 0:
            #  방향기준 앞 O -> 전진 -> 청소
            if not dfs(nr, nc, nd):
               return False

      return True

N, M = map(int, input().split())
R, C, D = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
clean = 0

dfs(R, C, D)
print(clean)










