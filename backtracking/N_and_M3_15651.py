# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# # ver 1 
# def backtrack(k, lst):
#     # 가지 치기 
#     if k > M:
#         return 
#     # 정답 조건에 맞으면 출력 
#     if k == M:
#         print(*lst)
#         return 
    
#     for i in range(1, N + 1):
#         # 방문 처리 없음 
#         lst.append(i)
#         backtrack(k + 1, lst)
#         lst.pop()

# N, M = map(int, input().split())
# used = [0] * (N + 1)
# backtrack(0, [])


# ver 2 : '가능한' '모든' 경우 
def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return 

    for j in range(1, N + 1):
        dfs(n + 1, lst + [j])

N, M = map(int, input().split())
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)














