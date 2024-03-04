# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열 

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












