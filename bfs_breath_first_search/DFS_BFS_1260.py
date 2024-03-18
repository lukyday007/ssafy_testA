# 정점 개수 N, 간선 개수 M, 탐색 시작할 정점의 번호 V

# ver 1 : DFS
def DFS(start, lst):
   used = [0] * (N + 1)
   st = []
   used[start] = 1
   lst.append(start)

   while True:
      G[start].sort()
      for w in G[start]:
         if used[w] == 0:
            lst.append(w)
            st.append(start)
            start = w
            used[start] = 1
            break
            
      else:
         if st:
            start = st.pop()
         else:
            break
   
   return lst

# ver 2 : BFS
from collections import deque

def BFS(start, lst):
   used = [0] * (N + 1)
   Q = deque()
   used[start] = 1
   Q.append(start)
   lst.append(start)

   while Q:
      start = Q.popleft()
      G[start].sort()
      for w in G[start]:
         if used[w] == 0:
            used[w] = 1
            Q.append(w)
            lst.append(w)

   return lst

N, M, V = map(int, input().split()) 
G = [[] for _ in range(N + 1)]
for _ in range(M):
   a, b = map(int, input().split())
   G[a].append(b)
   G[b].append(a)

print(' '.join(map(str, (DFS(V, [])))))
print(' '.join(map(str, (BFS(V, [])))))


