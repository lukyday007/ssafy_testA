# 파이프 옮기기 

# ver 2 : DFS
# dr = [0, 1, 1]
# dc = [1, 1, 0]

# def dfs(r, c, d):
#    global cnt 

#    if r == N - 1 and c == N - 1:
#       if home[N-1][N-1] == 1:
#          cnt = 0
#          exit()
#       cnt += 1
#       return 
   
#    s, e = 0, 0
#    # 현재 위치, 방향 
#    if d == 0:       # 가로: 가로, 대각선
#       s, e = 0, 2
#    elif d == 1:     # 대각선: 가로, 대각선, 세로
#       s, e = 0, 3
#    else:             # 세로: 대각선, 세로 
#       s, e = 1, 3 

#    for nd in range(s, e):
#       nr = r + dr[nd]
#       nc = c + dc[nd]
#       # 벽이 긁히지 않게          
#       if nr >= N or nc >= N: continue
#       # 주변에 방해물이 있는지 
#       if nd == 1:
#          if home[r + 1][c] != 0 or  home[r][c + 1] != 0 or home[nr][nc] != 0: continue
#       else:
#          if home[nr][nc] != 0:  continue
      
#       # 2차원 배열로 방문 체크
#       if not home[nr][nc]:
#          home[nr][nc] = 2
#          dfs(nr, nc, nd)
#          home[nr][nc] = 0
      
# cnt = 0
# N = int(input())
# home = [list(map(int, input().split())) for _ in range(N)]
# visit = [[0] * N for _ in range(N)]
# cnt = 0
# visit[0][0] = 2
# visit[0][1] = 2
# dfs(0, 1, 0)
# print(cnt)



# ver 2 
def dfs(r, c, d):
   global cnt 

   if r == N - 1 and c == N - 1:
      cnt += 1
      return 
   
   # 대각선 : d = 2
   if d == 0 or d == 1 or d == 2:
      if r + 1 < N and c + 1 < N:
         if home[r][c + 1] == 0 and home[r + 1][c] == 0 and home[r + 1][c + 1] == 0:
            dfs(r + 1, c + 1, 2) 
   # 가로 : d = 0
   if d == 0 or d == 2: # 가로 -> 가로, 대각선
      if c + 1 < N:
         if home[r][c + 1] == 0:
            dfs(r, c + 1, 0)
   # 세로 : d = 1
   if d == 1 or d == 2: # 세로 -> 세로, 대각선 
      if r + 1 < N:
         if home[r + 1][c] == 0:
            dfs(r + 1, c, 1)

cnt = 0
N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
dfs(0, 1, 0)
print(cnt)


# def dfs(r, c, d):
#    global cnt

#    if r == N - 1 and c == N - 1:
#       if home[N - 1][N - 1] == 1:  
#          cnt = 0
#          return
#       cnt += 1
#       return

#    if r + 1 < N and c + 1 < N and home[r][c + 1] == 0 and home[r + 1][c] == 0 and home[r + 1][c + 1] == 0:
#       home[r+1][c+1] = 2
#       dfs(r + 1, c + 1, 2)
#       home[r+1][c+1] = 0

#    if d == 0 or d == 2:  
#       if r + 1 < N and home[r + 1][c] == 0:
#          home[r+1][c] = 2
#          dfs(r + 1, c, 0)
#          home[r+1][c] = 0

#    if d == 1 or d == 2:  
#       if c + 1 < N and home[r][c + 1] == 0:
#          home[r][c+1] = 2
#          dfs(r, c + 1, 1)
#          home[r][c+1] = 0

# N = int(input())
# home = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# home[0][0] = 2
# home[0][1] = 2
# dfs(0, 1, 0)
# print(cnt)
