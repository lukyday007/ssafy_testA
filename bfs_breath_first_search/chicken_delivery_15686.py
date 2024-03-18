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

def dfs_and_bfs(s, points, dist):
   if s > M:
      return 

   if len(points) <= M:
      print(points)
      return 
   
   dfs_and_bfs(s + 1, points, dist)
   dfs_and_bfs(s + 1, points + [chicken[s]], dist)

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
visited = [0] * (len(chicken) + 1)

for r in range(N):
   for c in range(N):
      if city[r][c] == 2:
         chicken.append((r, c))
print(chicken)

dfs_and_bfs(0, [], 0)




