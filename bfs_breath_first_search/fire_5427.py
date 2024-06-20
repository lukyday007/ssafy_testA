# from collections import deque
# # 벽에는 불이 붙지 않는다.
# # 상근이는 벽을 통화할 수 없고
# # 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다
# # . : 빈 공간
# # # : 벽
# # @ : 상근이의 위치
# # * : 불 
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def BFS(Q, P): # Q = fire, P = exit route
#    visited = [[False] * C for _ in range(R)]

#    time = 0
#    while True:
#       while Q: # fire
#          cr, cc, ct = Q.popleft()
#          if ct == time:
#             for d in range(4):
#                nr = cr + dr[d]
#                nc = cc + dc[d]
#                nt = ct + 1
#                if 0 <= nr < R and 0 <= nc < C:
#                   if mp[nr][nc] == ".":
#                      if nr in [0, R-1] or nc in [0, C-1]:                        
#                         return "IMPOSSIBLE"
#                      Q.append((nr,nc,nt))
#                      mp[nr][nc] = "*" 
#          else:
#             Q.append((cr, cc, ct))
#             break
      
#       # for r in range(R):
#       #    print(*mp[r])
#       # print()
      
#       while P: # exit route
#          cr, cc, ct = P.popleft()
#          mp[cr][cc] = "."
#          if ct == time:
#             for d in range(4):
#                nr = cr + dr[d]
#                nc = cc + dc[d]
#                nt = ct + 1

#                if 0 <= nr < R and 0 <= nc < C:
#                   if mp[nr][nc] == "." and not visited:
#                      # 탈출 조건 : 둘 중 하나의 좌표에 0, R-1, C - 1
#                      if nr in [0, R-1] or nc in [0, C-1]:                        
#                         return nt + 1
                     
#                      P.append((nr,nc,nt))
#                      mp[nr][nc] = "@"
#                      visited[nr][nc] = True
#          else:
#             P.append((cr, cc, ct))
#             mp[cr][cc] = "@"
#             break

#       time += 1

#       if not P:   # 더 이상 갈 곳이 없을 때 
#          return "IMPOSSIBLE"

# for _ in range(int(input())):
#    C, R = map(int, input().split())
#    mp = [list(input()) for _ in range(R)]

#    person = deque((r,c,0) for r in range(R) for c in range(C) if mp[r][c] == '@')
#    fires = deque((r,c,0) for r in range(R) for c in range(C) if mp[r][c] == '*')

#    print(BFS(fires, person))















from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS(Q, P): # Q = fire, P = exit route
   global fires, person
   visited = [[False] * C for _ in range(R)]

   time = 0
   while True:
      while Q: # fire
         cr, cc, ct = Q.popleft()
         if ct == time:
            for d in range(4):
               nr = cr + dr[d]
               nc = cc + dc[d]
               nt = ct + 1
               if 0 <= nr < R and 0 <= nc < C:
                  if mp[nr][nc] == "." and not visited[nr][nc]:

                     Q.append((nr,nc,nt))
                     mp[nr][nc] = "*" 
                     visited[nr][nc] = True
         else:
            Q.append((cr, cc, ct))
            break
      
      while P: # exit route
         cr, cc, ct = P.popleft()
         # mp[cr][cc] = "."
         if ct == time:
            for d in range(4):
               nr = cr + dr[d]
               nc = cc + dc[d]
               nt = ct + 1

               if 0 <= nr < R and 0 <= nc < C:
                  if mp[nr][nc] == "." and not visited[nr][nc]:
                     P.append((nr,nc,nt))
                     mp[nr][nc] = "@"
                     visited[nr][nc] = True
                  
               # 탈출 조건 : 둘 중 하나의 좌표에 0, R-1, C - 1
               # 사실 탈출 조건은 위에 해당하는 것이 아니라, 그 바깥의 범위로 나가면 되는 것!!!!!!!! 
               else:                        
                  return nt
                     

         else:
            P.append((cr, cc, ct))
            break

      time += 1

      if not P:   # 더 이상 갈 곳이 없을 때 
         return "IMPOSSIBLE"

for _ in range(int(input())):
   C, R = map(int, input().split())
   mp = [list(input()) for _ in range(R)]

   person = deque((r,c,0) for r in range(R) for c in range(C) if mp[r][c] == '@')
   fires = deque((r,c,0) for r in range(R) for c in range(C) if mp[r][c] == '*')

   print(BFS(fires, person))



'''
1
5 5
....*
...@#
....#
....#
...#.
'''



