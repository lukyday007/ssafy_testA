# 
import sys
sys.setrecursionlimit(10**6)

def dfs(r, c):
   if r < 0 or r >= N or c < 0 or c >= N or visited[r][c] == 1: return False

   if game[r][c] == -1:
      return True
   
   visited[r][c] = 1
   return dfs(r + game[r][c], c) or dfs(r, c + game[r][c])

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

if dfs(0, 0):
   print("HaruHaru")
else:
   print("Hing")




