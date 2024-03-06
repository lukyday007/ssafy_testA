# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열 
# ver 1 
def backtrack(k, lst):
    # 임시 리스트의 길이를 기저 조건으로 
    if len(lst) == M:
        print(*lst)
        return 

    for i in range(1, N + 1):
        # 방문 처리를 함으로 1,1/ 2,2/ 3,3 같은 중복 제거 
        if used[i] == 0:
            used[i] = 1
            backtrack(i + 1, lst + [i])
            used[i] = 0

N, M = map(int, input().split())
used = [0] * (N + 1)
backtrack(0, [])

# ver 2
def dfs(n, lst):
    # 종료 조건 (n에 관련) 처리 + 정답 처리 
    if n == M:  # M개의 수열을 완성 
        ans.append(lst) 
        return 
    
    # 하부 단계 (함수) 호출
    for j in range(1, N + 1):
        if v[j] == 0:   # 선택하지 않은 숫자인 경우 추가 
            v[j] = 1
            dfs(n + 1, lst + [j])
            v[j] = 0

N, M = map(int, input().split())
ans = []            # 정답 리스트를 저장할 리스트 
v = [0] * (N + 1)   # 중복 확인을 위한 visited[]
dfs(0, [])
for lst in ans:
    print(*lst)











