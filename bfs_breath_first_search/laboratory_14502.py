# 연구소 
# # ver 1 
# from collections import deque
# import copy
# # 세울 수 있는 벽이 3개 = 깊이가 3인 DFS
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def BFS(Q, labo):
#    cnt = 0     # 퍼진 바이러스 세기

#    while Q:
#       cr, cc = Q.popleft()
#       for d in range(4):
#          nr = cr + dr[d]
#          nc = cc + dc[d]
#          if 0 <= nr < N and 0 <= nc < M:
#             if labo[nr][nc] == 0:
#                labo[nr][nc] = 2
#                cnt += 1
   
#    labo = oriLabo    # 초기화
#    return cnt
            

# def DFS(k, r, c):
#    global maxV, wall

#    if k == 3:
#       result = BFS(virus, labo) # 퍼진 바이러스의 총 개수
#       print(f"result: {result}")
#       res = M * N - (result + virus_cnt) - wall - 3
#       if maxV > res:
#          return
#       maxV = max(res, maxV)
#       return 
   
#    for d in range(4):
#       nr = r + dr[d]
#       nc = c + dc[d]
#       if 0 <= nr < N and 0 <= nc < M:
#          if labo[nr][nc] == 0:
#             labo[nr][nc] = 1
#             DFS(k + 1, nr, nc)
#             labo[nr][nc] = 0

# N, M = map(int, input().split())
# labo = [list(map(int, input().split())) for _ in range(N)]
# oriLabo = copy.deepcopy(labo) # 초기화용 
# wall = 0
# maxV = 0

# virus = deque()
# for n in range(N):
#    for m in range(M):
#       if labo[n][m] == 2:  # 바이러스 좌표 넣기
#          virus.append((n, m))
#       elif labo[n][m] == 1:   # 벽 개수 세기 
#          wall += 1

# virus_cnt = len(virus)
# ans = 0
# for r in range(N):
#    for c in range(M):
#       if labo[r][c] == 0:
#          ans = DFS(0, r, c)
#          break

# print(ans)


# ver 2 
# 벽을 세울 위치 튜플 리스트 -> 길이 3 -> DFS (조합)
# 바이러스 위치 튜플 리스트 -> BFS -> 바이러스 퍼지게 하기 
from collections import deque
import copy 
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def BFS(Q, arr):  # Q 는 바이러스, arr 은 lab
   cnt = len(virus)

   while Q: 
      cr, cc = Q.popleft()
      for d in range(4):
         nr = cr + dr[d]
         nc = cc + dc[d]
         if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] == 0:
               arr[nr][nc] = 2 
               cnt += 1

   return cnt


def DFS(k, r, c):
   global maxV, wall

   if k == 3:
      virus_cnt = BFS(virus, copy.deepcopy(lab))
      wall += k
      if maxV > (R * C - virus_cnt - wall):
         return  
      maxV = max(maxV, (R * C - virus_cnt - wall))
      return 
   
   for nr in range(R):
      for nc in range(C):
         if 0 <= nr < R and 0 <= nc < C:
            if lab[nr][nc] == 0:
               lab[nr][nc] = 1
               DFS(k + 1, nr, nc)
               lab[nr][nc] = 0


R, C = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(R)]
oriLabo = copy.deepcopy(lab) # 초기화용 
maxV = 0
wall = 0

virus = deque()
for r in range(R):
   for c in range(C):
      if lab[r][c] == 2:
         virus.append((r, c))
      elif lab[r][c] == 1:
         wall += 1
      

DFS(0, 0, 0)
print(maxV)












