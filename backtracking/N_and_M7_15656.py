# ver 1

def backtrack(k, lst):
    if k == M:
        print(*lst)
        return 
    
    for i in range(N):
        backtrack(k + 1, lst + [arr[i]])

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0] * (N + 1)
backtrack(0, [])
