# ver 1 : Fail
from collections import deque
def BFS(N, K):
   Q = deque()
   Q.append((N, 0))
   used[N] = 1

   while Q:
      N , move = Q.popleft()
      if N == K:
         return move

      for d in (N - 1, N + 1, 2*N):
         # 이럴 경우 d가 범위를 초과하면 바로 indexerror 발생 -> 분리 필요
         if used[d] == 0 and 0 <= d < 100001:
            used[d] = 1
            Q.append((d, move + 1))   

N, K = map(int, input().split())
used = [0] * 100001
print(BFS(N, K))

# ver 2 : pass 
from collections import deque

def BFS(N, K):
    Q = deque()
    Q.append((N, 0))
    used = [0] * 100001
    used[N] = 1

    while Q:
        N, move = Q.popleft()
        if N == K:
            return move

        for d in (N - 1, N + 1, 2 * N):
            if 0 <= d < 100001:
                if used[d] == 0:
                    used[d] = 1
                    Q.append((d, move + 1))

N, K = map(int, input().split())
print(BFS(N, K))