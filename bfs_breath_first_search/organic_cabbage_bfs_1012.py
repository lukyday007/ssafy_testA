# ver 2 : 방문 체크의 중요성... 너무나 중요 *****
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    visited[r][c] = 1
    # 배추 있는지 없는지 확인
    flag = False 

    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 체크 
            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue
            # 방문 안했고, 배추 있으면 방문 표시, 배추 True
            if visited[nr][nc] == 0 and farm[nr][nc] == 1:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                flag = True
    # 배추 있으면 1리턴
    if flag:
        return 1
    # 없으면 0
    return 0

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    for _ in range(K):
        r, c = map(int, input().split())
        farm[r][c] = 1

    ans = 0
    for r in range(len(farm)):
        for c in range(len(farm[r])):
            if visited[r][c] == 0 and farm[r][c] == 1:
                # 좌표를 돌며 함수 실행, 결과 누적
                ans += 1
                bfs(r,c)
    print(ans)






