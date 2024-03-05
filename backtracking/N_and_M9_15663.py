def backtrack(k, tlst):
    if k == M:
        settoList.add(tuple(tlst[:]))
        return 
    
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            backtrack(k + 1, tlst + [arr[i]])
            used[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0] * N
settoList = set()
backtrack(0, [])
lst = sorted(list(settoList))
for l in lst:
    print(*l)