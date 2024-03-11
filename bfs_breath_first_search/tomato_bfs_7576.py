# # ver 1
# from collections import deque
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def bfs(tomatos):
#    Q = deque()
#    for r, c in tomatos:
#       visited[r][c] = 1
#       Q.append((r, c))
#    val = 0
#    while Q:
#       r, c = Q.popleft()
#       for d in range(4):
#          nr = r + dr[d]
#          nc = c + dc[d]
#          if nc < 0 or nc >= C or nr < 0 or nr >= R: continue
#          if visited[nr][nc] == 0 and farm[nr][nc] == 0:
#             Q.append((nr, nc))
#             visited[nr][nc] = visited[r][c] + 1
#             val = visited[nr][nc] - 1
            
#    return val 

# C, R = map(int, input().split())
# farm = [list(map(int, input().split())) for _ in range(R)]
# # -1 이 0으로 처리는 되는 걸 방지하기 위해 farm 을 그래도 받아옴 
# visited = [[0] * C for _ in range(R)]
# # 익은 토마토 좌표 저장 
# ripedT = []
# for r in range(R):
#    for c in range(C):
#       if farm[r][c] == 1:
#          ripedT.append((r, c))

# ans = bfs(ripedT)
# # 토마토가 익지 않았을 때 
# for r in range(R):
#    for c in range(c):
#       if visited[r][c] == 0 and farm[r][c] != -1:
#          ans = -1

# # 이미 모든 토마토가 익었을 때 
# for f in farm:
#    if 0 not in f:
#       ans = 0

# print(ans)


# ver 2
# 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있음 
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸 


# -1 이 0으로 처리는 되는 걸 방지하기 위해 farm 을 그래도 받아옴  

from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(visited, riped_tomatoes, farm):
    Q = deque()
    for r, c in riped_tomatoes:
        Q.append((r, c))
        visited[r][c] = 1
    
    move = 0
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if visited[nr][nc] == 0 and farm[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                move = visited[nr][nc] - 1
    
    for v in visited:
        if 0 in v:
            return -1
        
    return move

def get_answer(r, c):
    farm = [list(map(int, input().split())) for _ in range(R)]

    # 덜익은 토마토가 없는 상태 
    ripe = False
    riped_tomatoes = []
    no_tomato = []
    for r in range(R):
        for c in range(C):
            # 덜 익은 토마토가 있으면 True
            if farm[r][c] == 0:
                ripe = True
            # 익은 토마토 좌표 놓기 -> BFS 사용
            elif farm[r][c] == 1:
                riped_tomatoes.append((r, c))
            # 토마토 없는 좌표 -> visited 에 넣기 
            elif farm[r][c] == -1:
                no_tomato.append((r, c))

    # 덜익은 토마토가 없으면 계속 False -> 0 출력 
    if not ripe:
        print(0)
        return
    
    # 토마토가 모두 익지 못하는 상황이면 -1 출력
    visited = [[0] * C for _ in range(R)]
    for r, c in no_tomato:
        visited[r][c] = -1

    print(bfs(visited, riped_tomatoes, farm))

C, R = map(int, input().split())
get_answer(R, C)



