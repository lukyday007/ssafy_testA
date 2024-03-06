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

N, M = map(int, input().split())
used = [0] * (N + 1)
backtrack(0, [])


# ver 2 : 정해진 곳에서 종료 조건을 설정, 방문 처리 X
# 이진 트리 방식으로 풀이 : 선택하냐, 선택 안하냐 
# n : 선택할 숫자 (1 ~ N)
# N에 대한 모든 조건을 돌 것 -> n > N 
def dfs(n, lst):
    if n > N:   # n관련된 종료조건 => 종료조건 != 정답처리
        if len(lst) == M:   # M 개 자리 수열 => 정답 처리 
            ans.append(lst)
        return 
    
    dfs(n + 1, lst + [n])   # 선택하는 경우
    dfs(n + 1, lst)         # 선택하지 않는 경우 

N, M = map(int, input().split())
ans = []
dfs(1, [])  # for 반복문이 아닌, 있는지 없는지 여서 0이 아닌, 1로 시작 
for lst in ans:
    print(*lst)











