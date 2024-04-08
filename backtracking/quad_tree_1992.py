# N은 언제나 2의 제곱수 
#  -> 병렬 구조, 혹은 분할적으로 접근할 수 있는 힌트! 
# 왼쪽 위,     오른쪽 위
# 왼쪽 아래,   오른쪽 아래

def divide_conquer(SR, ER, SC, EC, string):
   # 기저 조건 
   if SR + 1 == ER and SC + 1 == EC:
      return string

   # 일반 사례 : 분할 
   MR = (SR + ER) // 2
   MC = (SC + EC) // 2

   if SR >= ER or SC >= EC:
      return "(" + LU + RU + LD + RD + ")"

   # 작업 시작 
   LU = divide_conquer(SR, MR, SC, MC, string)
   RU = divide_conquer(SR, MR, MC, EC, string)
   LD = divide_conquer(MR, ER, SC, MC, string)
   RD = divide_conquer(MR, ER, MC, EC, string) 

   # 왼쪽 위 
   for r in range(SR, (SR + ER)//2):
      for c in range(SC, (SC + EC)//2):
         string += str(board[r][c])

   # 오른쪽 위 
   for r in range(SR, (SR + ER)//2):
      for c in range((SC + EC)//2, EC):
         string += str(board[r][c])

   # 왼쪽 아래
   for r in range((SR + ER)//2, ER):
      for c in range(SC, (SC + EC)//2):
         string += str(board[r][c])

   # 오른쪽 아래
   for r in range((SR + ER)//2, ER):
      for c in range((SC + EC)//2, EC):
         string += str(board[r][c])

   string = set(list(string))
   string = ''.join(map(str, string ))

   print(f"string : {string}")
   return string

board = [
   [0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0],
   [0,0,0,0,1,1,1,1],
   [0,0,0,0,1,1,1,1],
   [0,0,0,1,1,1,1,1],
   [0,0,1,1,1,1,1,1],
   [0,0,1,1,1,1,1,1],
   [0,0,1,1,1,1,1,1]
]

SR, ER, SC, EC = 0, len(board), 0, len(board[0])
print(divide_conquer(SR, ER, SC, EC, ""))


def divide_conquer(SR, ER, SC, EC, board):
   # 기저 조건 
   if SR + 1 == ER and SC + 1 == EC:
      return str(board[SR][SC])

   # 분할
   MR = (SR + ER) // 2
   MC = (SC + EC) // 2

   LU = divide_conquer(SR, MR, SC, MC, board)
   RU = divide_conquer(SR, MR, MC, EC, board)
   LD = divide_conquer(MR, ER, SC, MC, board)
   RD = divide_conquer(MR, ER, MC, EC, board)
   
   # 합치기
   if LU[0] == RU[0] == LD[0] == RD[0] and len(LU) == len(RU) == len(LD) == len(RD) == 1:
      return LU[0]
   else:
      return "(" + LU + RU + LD + RD + ")"

N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]

SR, ER, SC, EC = 0, N, 0, N
print(divide_conquer(SR, ER, SC, EC, board))














