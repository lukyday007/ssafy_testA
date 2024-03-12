# ver 1 
from collections import deque
N = int(input())
visited = [0] * 51

while True:
   a, b = map(int, input().split())
   if a == -1:
      break
   visited[a] += 1
   visited[b] += 1

print(visited[1:])

maxV = max(visited)
minV = 50
res = []
for i, v in enumerate(visited):
   if maxV < minV:
      minV = maxV
      res = [i]
   elif minV == maxV:
      res.append(i)

print(minV, len(res))
print(*res)


# # ver 2 
# 노드별 최대 거리
# n번의 bfs를 돌리고
# 후보와 회원들의 간선 거리를 측정, 제일 적으면 -> 출력
from collections import deque

def bfs(graph, num):
   Q = deque()
   visited = [0] * (N + 1)
   visited[num] = 1
   Q.append(num)
   maxV = 0
   while Q:
      v = Q.popleft()
      for w in graph[v]:
         if not visited[w]:
            Q.append(w)
            visited[w] = visited[v] + 1
            maxV = visited[w] - 1
   return maxV
            
N = int(input())
G = [[] for _ in range(51)]

# 입력된 정보로 무향그래프 완성
while True:
   a, b = map(int, input().split())
   if a == -1:
      break
   G[a].append(b)
   G[b].append(a)

minV = 51
candidates = []
for i in range(1, N + 1):
   # tmp: visited list
   tmp = bfs(G, i)
   if minV > tmp:
      candidates = [i]
      minV = tmp
   elif minV == tmp:
      candidates.append(i)

print(minV, len(candidates))
print(*candidates)





# minV = 50
# for g in range(len(G)):
#    if maxV < len(G[g]):
#       maxV = len(G[g])  

# res = []
# for g in range(len(G)):
#    if len(G[g]) == maxV:
#       res.append(g)

# print(N - maxV, len(res))
# print(" ".join(map(str, res)))

# 1점 : 어느 회원이 다른 모든 회원과 친구
# 2점 : 어른 회원이 다른 모든 회원의 친구이거나 친구의 친구
# 3점 : 어른 회원이 다른 모든 회원의 친구이거나 친구의 친구, 친구의 친구








