import copy
def checking_film(board):
   for c in range(C):
      tmp = 1
      for r in range(R - 1):
         if board[r][c] == board[r + 1][c]:
            tmp += 1
            if tmp >= K:
               break
         else:
            tmp = 1

      if tmp < K:
         return False
   return True

def inputting(r, attr, board):
   for c in range(C):
      board[r][c] = attr
   return board  

def dfs(r, cnt, board): # 행, 특성, 횟수, 배열 
   global minV

   if minV < cnt:
      return 

   if checking_film(board):
      minV = min(minV, cnt)
      return 
   
   if r == R:  # 기저 조건 
      return 
   
   dfs(r + 1, cnt, board)  # 아무 약품도 투입 X
   
   dfs(r + 1, cnt + 1, inputting(r, 0, copy.deepcopy(board)))  # 0 약품을 투입할 때 
   
   dfs(r + 1, cnt + 1, inputting(r, 1, copy.deepcopy(board)))  # 1 약품을 투입할 때 

for tc in range(1, int(input()) + 1):
   R, C, K = map(int, input().split())
   film = [list(map(int, input().split())) for _ in range(R)]
   oriFilm = copy.deepcopy(film)
   minV = K
   dfs(-1, 0, film)
   print(f'#{tc} {minV}')


import copy
def checking_film(board):
   for c in range(C):
      tmp = 1
      for r in range(R - 1):
         if board[r][c] == board[r + 1][c]:
            tmp += 1
            if tmp >= K:
               # 두 번째 반복문이 종료, 첫 번째로 다시 돌아감
               break    
         else:
            tmp = 1

      if tmp < K:
         return False
   return True

def dfs(r, cnt, board): # 행, 특성, 횟수, 배열 
   global minV

   if cnt >= minV:
      return 

   if checking_film(board):
      minV = min(minV, cnt)
      return 
   
   if r == R:  # 기저 조건 
      return 
   
   dfs(r + 1, cnt, board)  # 아무 약품도 투입 X
   
   film[r] = a_type
   dfs(r + 1, cnt + 1, film)  # A 약품을 투입할 때 
   
   film[r] = b_type
   dfs(r + 1, cnt + 1, film)  # B 약품을 투입할 때 

   film[r] = oriFilm[r] # 초기화 

for tc in range(1, int(input()) + 1):
   R, C, K = map(int, input().split())
   film = [list(map(int, input().split())) for _ in range(R)]
   oriFilm = copy.deepcopy(film)
   a_type = [0] * C
   b_type = [1] * C
   minV = K
   dfs(-1, 0, film)
   print(f'#{tc} {minV}')




def checkingf_film(board):
   check = [0] * C
   for c in range(C):
      tmp = 1
      for r in range(R - 1):
         if board[r][c] == board[r + 1][c]:
            tmp += 1
            if tmp >= 3:
               check[c] = tmp
               continue
         else:
            tmp = 1

   flag = False             
   for c in check:
      if c < 3:
         flag = True
   
   if flag:
      return False 
   
   return True  

def inputting(r, attr, board):
   for c in range(C):
      board[r][c] = attr
   return board  

def dfs(r, att, cnt, board): # 행, 특성, 횟수, 배열 
   global minV

   if r == R:  # 기저 조건 
      return 
   if checkingf_film(board):
      minV = min(minV, cnt)
      return 
   
   if att != -1:
      board = inputting(r, att, board)
   
   dfs(r + 1, -1, cnt, board)  # 아무 약품도 투입 X
   
   dfs(r + 1, 0, cnt + 1, board)  # 0 약품을 투입할 때 
   
   dfs(r + 1, 1, cnt + 1, board)  # 1 약품을 투입할 때 


R, C, K = map(int, input().split())
film = [list(map(int, input().split())) for _ in range(R)]
visited = [0] * R
minV = 21e18
print(checkingf_film(film))
dfs(-1, -1, 0, film)
print(minV)
