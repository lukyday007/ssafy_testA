# # ver 1 : 틀릴 줄 알았는데 그냥 제출해봤음 
# # 국어를 잘하자
# # 답 조건: 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 뭍혀있다
# from collections import deque
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def bfs(r, c, v):
#     Q = deque()
#     visited = [[0] * C for _ in range(R)]
#     Q.append((r, c))
#     visited[r][c] = 1

#     while Q:
#         r, c = Q.popleft()
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]

#             if nr < 0 or nr >= R or nc < 0 or nc >= C:
#                 continue

#             if visited[nr][nc] == 0 and mp[nr][nc] == "L":
#                 Q.append((nr, nc))
#                 visited[nr][nc] = visited[r][c] + 1
#                 v += 1
#     return v 

# R, C = map(int, input().split())
# mp = [list(input()) for _ in range(R)]

# minV = 1000
# for r in range(R):
#     for c in range(C):
#         if mp[r][c] == "L":
#             tmp = bfs(r, c, 0)
#             minV = min(tmp, minV)
# print(tmp)


# ver 2
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c, v):
    global tmpList
    tmpSet = set()
    Q = deque()
    Q.append((r, c))
    visited[r][c] = 1
    tmpSet.add((r, c))
    v += 1

    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue

            if visited[nr][nc] == 0 and mp[nr][nc] == "L":
                Q.append((nr, nc))
                visited[nr][nc] = 1
                tmpSet.add((nr, nc))
                v += 1

    tmpList.append(tmpSet)
    return v

R, C = map(int, input().split())
mp = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

tmpList = []
for r in range(R):
    for c in range(C):
        if mp[r][c] == "L" and visited[r][c] == 0:
            bfs(r, c, 0)

print(tmpList)
print(len(tmpList))

maxV = 0
for tmp in tmpList:
    minV = 1000
    for t in list(tmp):
        visited = [[0] * C for _ in range(R)]
        r, c = t
        tmV = bfs(r, c, 0)
    minV = min(tmV, minV)
maxV = max(maxV, minV)
print(maxV)



