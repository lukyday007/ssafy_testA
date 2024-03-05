# ver 1
def backtrack(k, s, lst):
    if k == M:
        print(*lst)
        return 
    
    for i in range(s, N):
        backtrack(k + 1, i, lst + [arr[i]])

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
backtrack(0, 0, [])