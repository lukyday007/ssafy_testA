# ver 1 :   check -> dir, length 
#           set_line -> board 표시 
#     상  하 좌 우 
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# # 각 방향에 대한 방문 표시 
# # visited_direction = [0,0,0,0]
# def check(cr, cc, dir):    # 전선을 놓을 방향과 길이 반환 
#    # 4 방향으로 진행 
#    for d in range(4):
#       # 방문하지 않은 방향
#       length = 0
#       if not dir[d]:
#          nr, nc = cr, cc
#          flag = True 
#          while flag:

#             nr += dr[d]
#             nc += dc[d]
#             if nr in [-1, N] or nc in [-1, N]:
#                break
#             length += 1
#             # 이미 회로에 코어나 전선이 놓여 있을 때 
#             if board[nr][nc] != 0:
#                dir[d] = -1
#                flag = False 

#          if flag:            
#             return d, length
         
#    return -1, 0
            
# def set_line(d, r, c, on_off): 
#    if d in (0, 2):   # 상, 좌  
#       while True:
#          r += dr[d]
#          c += dc[d]
#          if r == -1 or c == -1:
#             break
#          board[r][c] = on_off
#    else:
#       while True:   # 하, 우  
#          r += dr[d]
#          c += dc[d]
#          if r == N or c == N:
#             break
#          board[r][c] = on_off

# def backtrack(k, core, cd, dir, L):
#    global minV, maxC   
#    print(k, core)
#    if k == C:
#       if core < maxC:
#          return 
#       else:
#          if core > maxC:
#             maxC = core 
#             minV = L 
#          else:
#             minV = min(minV, L)
      
#       return 

#    cr, cc, dir = cores[k]  # cores unpacking
#    nd, length = check(cr, cc ,dir)
#    # 전선을 놓을 방향이 있을 때 
#    if nd != -1:
#       # 방향 방문 처리 
#       dir[nd] = 1
#       print()
#       print(f"nd : {nd}, cr : {cr}, cc : {cc}")
#       print(f"dir : {dir}, length: {L + length}")
#       # 보드에 전선 놓기 
#       set_line(nd, cr, cc, 2)

#       for b in board:
#          print(*b)
#       print()
#       backtrack(k + 1, core + 1, nd, dir, L + length)
#       # 보드에 전선 치우기 (보드 초기화)
#       set_line(nd, cr, cc, 0)
#       print(f"nd : {nd}, cr : {cr}, cc : {cc}")
#       print(f"dir : {dir}, length: {L}")
#       for b in board:
#          print(*b)
#       print()

#    backtrack(k + 1, core, cd, dir, L)

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# # 각 방향에 대한 방문 표시 
# # visited_direction = [0, 0, 0, 0]
# cores = [[r, c, [0, 0, 0, 0]] for r in range(N) for c in range(N) if board[r][c]]
# maxC = 0          # 최대 코어 개수 


# # 가장 자리에 있는 코어 먼저 더하기 
# for i in range(len(cores)-1, -1, -1):
#    if 0 in cores[i] or (N - 1) in cores[i]:
#       cores.pop(i)
#       maxC += 1

# C = len(cores)    # 코어 수 
# minV = N * C

# backtrack(0, maxC, -1, dir, 0)

# print()
# for b in board:
#    print(*b)
# print()

# print(minV)


# ver 2 : for 문으로 델타를 돌리면 visited_directions배열을 추가할 필요가 없음! 
# check -> return boolean
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 해당 방향에 코어나 전선이 있는지 확인 -> true/false 반환 
def possible(cr, cc, d):    
   while True:
      cr += dr[d]
      cc += dc[d] 
      if 0 <= cr < N and 0 <= cc < N:
         if board[cr][cc]:
            return False 
      else:
         break

   return True 
         
# 전선 놓고 빼기  -> 전선 길이 반환 
def set_line(d, r, c, on_off): 
   length = 0
   while True:
      r += dr[d]
      c += dc[d]
      if 0 <= r < N and 0 <= c < N:
         board[r][c] = on_off
         length += 1
      else:
         break
   return length 

def backtrack(lv, core, L):
   global minV, maxC   

   if C - lv + core < maxC:     # 여분의 코어 + 현재 코어 < 최대 코어 개수 
      return 

   if lv == C:
      if core < maxC:
         return 
      else:
         if core > maxC:
            maxC = core 
            minV = L 
         else:
            minV = min(minV, L)
      
      return 
   
   for d in range(4):
      cr, cc = cores[lv]
      if possible(cr, cc, d):
         length = set_line(d, cr, cc, 2)
         backtrack(lv + 1, core + 1, L + length)
         set_line(d, cr, cc, 0)

   backtrack(lv + 1, core, L)

for tc in range(1, int(input()) + 1):
   N = int(input())
   board = [list(map(int, input().split())) for _ in range(N)]
   cores = [(r, c) for r in range(N) for c in range(N) if board[r][c]]
   maxC = 0          # 최대 코어 개수 

   # 가장 자리에 있는 코어 먼저 더하기 
   for i in range(len(cores)-1, -1, -1):
      if 0 in cores[i] or (N - 1) in cores[i]:
         cores.pop(i)
         maxC += 1

   C = len(cores)    # 코어 수 
   minV = N * C

   backtrack(0, maxC, 0)
   print(f"#{tc} {minV}")

