# K 개의 미생물 군집
# 가로 N, 세로 N 
# 1시간마다 이동방향에 있는 다음 셀로 이동
# 맨 끝에 도달하면 미생물 절반이 죽고 //2, 이동방향이 반대로 바뀜
# 두 개 이상의 군집이 모이는 경우 합쳐짐, 이때 수가 많은 군집의 이동방향으로 바뀜 
# M 시간동안 미생물 군집 격리 -> 총합 구하기 
# 상 1 하 2 좌 3 우 4
from collections import deque

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
# 셀의 개수 : N, 격리 시간 : M, 미생물 군집의 개수 : K 
# 세로위치, 가로위치, 미생물 수, 이동방향 
#  r,       c,       n,         d 

def BFS(Q):
   while Q:
      # 3차원 배열 처리: 곂칠 때
      for r in range(R):
         for c in range(C):
            if cell[r][c] != -1 and len(cell[r][c]) > 1:



      # 현재 시간 == 격리시간일 때 정지 -> 셀 위에 남은 수 합치기 

      cr, cc, cn, cd, ct = Q.popleft()
      nr = cr + dr[cd]
      nc = cc + dc[cd]
      if cell[nr][nc] != -1:
         cell[nr][nc].append((cn, cd))
         Q.append((nr, nc, cn, cd, ct))
      else:
         if cd == 1:
            nd = 2
         elif cd == 2:
            nd = 1
         elif cd == 3:
            nd = 4
         else:
            nd = 3
         Q.append((nr, nc, cn//2, nd, ct + 1))
       

N, M, K = map(int, input().split())
cell = [[-1] * N] + [([-1] + [[]] * (N - 2) + [-1]) for _ in range(N - 2)] + [[-1] * N]

for c in cell:
   print(c)
Q = deque()
for _ in range(K):
   R, C, N, D = map(int, input().split())
   Q.append((R, C, N, D, 0))

print(Q)










