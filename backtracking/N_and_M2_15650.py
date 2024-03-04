# 중복되는 수열을 여러 번 출력되면 안됨
# 수열은 사전 순으로 증가
# ver 1
def backtrack(k, lst):
    if len(lst) == M:
        for i in range(1, len(lst)):
            # 오름차순 아닌 경우 가지치기 
            if lst[i] < lst[i - 1]:
                return
        print(*lst)
        return 
    for i in range(1, N + 1):
        if used[i] == 0:
            used[i] = 1
            backtrack(i + 1, lst + [i])
            used[i] = 0 

# N, M = map(int, input().split())
# used = [0] * (N + 1)
# backtrack(0, [])

# ver 2 : 정해진 곳에서 종료 조건을 설정 
# n : 선택할 숫자 (1 ~ N)
# N에 대한 모든 조건을 돌 것 -> n > N 

def dfs(n, lst):
    if n > N:   # n관련된 종료조건 => 종료조건 != 정답처리
        if len(lst) == M:   # M 개 자리 수열 => 정답 처리 
            ans.append(lst)
        return 
    
    dfs(n + 1, lst + [n])
    dfs(n + 1, lst)

N, M = map(int, input().split())
ans = []
dfs(1, [])
for lst in ans:
    print(*lst)











