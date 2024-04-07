# K 개의 미생물 군집
# 가로 N, 세로 N 
# 1시간마다 이동방향에 있는 다음 셀로 이동
# 맨 끝에 도달하면 미생물 절반이 죽고 //2, 이동방향이 반대로 바뀜
# 두 개 이상의 군집이 모이는 경우 합쳐짐, 이때 수가 많은 군집의 이동방향으로 바뀜 
# M 시간동안 미생물 군집 격리 -> 총합 구하기 
# 상 1 하 2 좌 3 우 4
# from collections import deque
# import copy

# dr = [0, -1, 1, 0, 0]
# dc = [0, 0, 0, -1, 1]
# mr = [0, 2, 1, 4, 3]    # 방향 전환 배열 
# # 셀의 개수 : N, 격리 시간 : M, 미생물 군집의 개수 : K 
# # 세로위치, 가로위치, 미생물 수, 이동방향 
# #  r,       c,       n,         d 

# def BFS(Q, M, S):
#    m = 0
#    while m < M:
#       cellDict = copy.deepcopy(oriCell)
#       # 현재 시간 == 격리시간일 때 정지 -> 셀 위에 남은 수 합치기 
#       idx = 0
#       while idx < len(Q):
#          cr, cc, cn, cd, ct = Q.popleft()
#          nr = cr + dr[cd]
#          nc = cc + dc[cd]
#           # 미생물이 절반으로, 반대 방향 
#          if nr == 0 or nr == S or nc == 0 or nc == S:
#             nd = mr[cd]
#             Q.append((nr, nc, cn//2, nd, ct + 1))
#          else:   
#             cellDict[(nr, nc)].append((cn, cd, ct + 1))
#             Q.append((nr, nc, cn, cd, ct + 1))

#          idx += 1 
       
#       # 미생물 움직임 처리 
#       for k in cellDict.keys():
#          if cellDict[k]:
#             maxV = 0
#             total = 0
#             fd = 0
#             ct = cellDict[k][0][-1]
#             for n, d, t in cellDict[k]:
#                total += n
#                if maxV < n:
#                   maxV = max(n, maxV)
#                   fd = d
#                Q.remove((k[0], k[1], n, d, t))

#             cellDict[k] = [(total, fd, ct)]
#             Q.append((k[0], k[1], total, fd, ct))

#       m += 1
   
#    # 남은 미생물 총합 구하기 
#    microbe = 0
#    for d in range(len(Q)):
#       microbe += Q[d][2]
   
#    return microbe

# for tc in range(1, int(input()) + 1):
#    S, M, K = map(int, input().split())

#    cellDict = {}
#    for r in range(1, S):
#       for c in range(1, S):
#          cellDict[(r, c)] = []  
#    oriCell = copy.deepcopy(cellDict)
   
#    Q = deque()
#    for _ in range(K):
#       R, C, N, D = map(int, input().split())
#       Q.append((R, C, N, D, 0))

#    print(f"#{tc} {BFS(Q, M, S)}")



dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
mr = [0, 2, 1, 4, 3]    # 방향 전환 배열 
# 셀의 개수 : N, 격리 시간 : M, 미생물 군집의 개수 : K 
# 세로위치, 가로위치, 미생물 수, 이동방향 
#  r,       c,       n,         d 

def solution(cellDict, M, S):
   m = 0
   while m < M:
      # 현재 시간 == 격리시간일 때 정지 -> 셀 위에 남은 수 합치기 
      for k in cellDict:
         if cellDict[k]:
            cr, cc = k
            cn, cd, ct = cellDict[k][0]
            cellDict[k] = []     # 초기화 

            nr = cr + dr[cd]
            nc = cc + dc[cd]
            # 미생물이 절반으로, 반대 방향 
            if nr == 0 or nr == S-1 or nc == 0 or nc == S-1:
               cd = mr[cd]
               cn //= 2

            cellDict[(nr, nc)].append((cn, cd, ct + 1))
      

      print("--------------------------")
      # 미생물 움직임 처리 
      for k in cellDict.keys():
         if cellDict[k]:
            maxV = 0
            total = 0
            fd = 0
            ct = cellDict[k][0][-1]
            for n, d, t in cellDict[k]:
               total += n
               if maxV < n:
                  maxV = max(n, maxV)
                  fd = d

            cellDict[k] = [(total, fd, ct)]
      
      for k in cellDict:
         if cellDict[k]:
            print(k)
            print(cellDict[k])
            print()

      m += 1
   
   # 남은 미생물 총합 구하기 
   microbe = 0
   for k in cellDict.keys():
      if cellDict[k]:
         microbe += cellDict[k][0][0]
   
   return microbe

S, M, K = map(int, input().split())

cellDict = {}
for r in range(S):
   for c in range(S):
      cellDict[(r, c)] = []  
      
for _ in range(K):
   R, C, N, D = map(int, input().split())
   cellDict[(R, C)].append((N, D, 0))

for k in cellDict:
   if cellDict[k]:
      print(k)
      print(cellDict[k])
      print()

print(solution(cellDict, M, S))
   # print(f"#{tc} {solution(cellDict, M, S)}")







