# 3. 지금까지 선택한 원소들의 합을 매개변수로 전달
# cur_sum: 0번 원소부터 k-1번 원소까지 선택한 원소들의 합
# arr = [1, 2, 3]
# N = len(arr)
# bits = [0] * N

# def backtrack(k, cur_sum, cur_cnt):
#    if k == N:
#       for i in range(N):
#          if bits[i] == 1:
#                print(arr[i], end=' ')
#       print()
#    else:
#       bits[k] = 1     # arr[k]를 부분집합에 포함
#       backtrack(k + 1, cur_sum + arr[k], cur_cnt + 1)
#       bits[k] = 0     # arr[k]를 포함하지 않음
#       backtrack(k + 1, cur_sum, cur_cnt)

# backtrack(0, 0, 0)
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def bfs(points):
   Q = deque()
   check = [[0] * N for _ in range(N)]
   val = 0
   for a, b in points:
      Q.append((a, b, 0))
      check[a][b] = 2
   
   while Q:
      r, c, pos = Q.popleft()
      for d in range(4):
         nr = r + dr[d]
         nc = c + dc[d]
         if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
         if check[nr][nc] == 0:
            check[nr][nc] = check[r][c] + 1
            Q.append((nr, nc, pos + 1))

            if city[nr][nc] == 1:
               val += (pos + 1)
               
   # for r in range(N):
   #    print(*check[r])
   # # print(f"val : {val}")
   # print()
   return val

def dfs(s, points):
   global minV
   if len(points) > M:
      return 
    
   if 0< len(points) <= M:
      tmp = points[:]
      # 여기서 bfs돌리기 
      tmpV = bfs(tmp)
      # print(f"tmpV: {tmpV}")
      if tmpV > 0:
         minV = min(minV , tmpV)

   for k in range(s, len(chicken)):
      if visited[k] == 0 and k < len(chicken):
         visited[k] = 1
         points.append(chicken[k])
         dfs(k + 1, points)
         points.pop()
         visited[k] = 0

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
minV = 21e18
for r in range(N):
   for c in range(N):
      if city[r][c] == 2:
         chicken.append((r, c))

visited = [0] * (len(chicken) + 1)
dfs(0, [])
print(minV)



# ver 2 : combination
from itertools import combinations
# 각 집 - 치킨 사이 거리를 구한뒤
# 조합으로 모든 m개의 치킨집을 뽑는 경우의 수를 구하여 치킨거리를 구한다
def solution(n, m, board):
    chickens = [] # 치킨집 (x,y)
    houses = [] # 집(x,y)
    dists = [] # dists[a][b] = a번째 치킨과 b번째 집간의 거리

    # 치킨집과 집 위치 저장
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                houses.append((i,j))
            if board[i][j] == 2:
                chickens.append((i,j))
    
    # 치킨집과 집간의 거리 저장
    for chicken in chickens:
        dist = []
        for house in houses:
            x = abs(chicken[0] - house[0])
            y = abs(chicken[1] - house[1])
            dist.append(x+y)
        dists.append(dist)

    # m개의 치킨집 뽑아 각 도시의 치킨거리 구하기
    result_comb = list(combinations(dists, m)) # m개를 뽑는 모든 조합 구하기
    result = 987654321
    for comb in result_comb:
        chicken_dist = [987654321] * len(comb[0])
        for c in comb:
            for i in range(len(c)):
                chicken_dist[i] = min(chicken_dist[i], c[i])
        result = min(result, sum(chicken_dist))
    
    return result

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
result = solution(n, m, board)
print(result)
