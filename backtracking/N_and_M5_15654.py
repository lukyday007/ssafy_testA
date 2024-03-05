# ver 1 
def backtrack(k, lst):
    if k == M:
        print(*lst)
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            lst.append(arr[i])
            backtrack(k + 1, lst)
            lst.pop()
            used[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used = [0] * (N + 1)
# backtrack(0, [])

# ver 2 : 리스트 + 정렬 내장함수 
def backtrack(k, lst):
    if k == M:
        print(*lst)
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            lst.append(arr[i])
            backtrack(k + 1, lst)
            lst.pop()
            used[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0] * (N + 1)
backtrack(0, [])




