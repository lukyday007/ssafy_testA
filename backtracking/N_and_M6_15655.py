# ver 1
# def backtrack(k, lst):
#     if k == M:
#         for i in range(1, len(lst)):
#             if lst[i] < lst[i - 1]:
#                 return 
#         print(*lst)
#         return 
    
#     for i in range(len(arr)):
#         if used[i] == 0:
#             used[i] = 1
#             lst.append(arr[i])
#             backtrack(k + 1, lst)
#             lst.pop()
#             used[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0] * (N + 1)
# backtrack(0, [])

# ver 2 : 증가하는 인덱스에 맞춰, 더할지, 말지 결정  
# def backtrack(k, lst):
#     if k > N - 1:   # 리스트 범위 주의! 
#         if len(lst) == M:
#             print(*lst)
#         return 
    
#     backtrack(k + 1, lst + [arr[k]])
#     backtrack(k + 1, lst)

# backtrack(0, [])

# ver 3
def backtrack(k, s, lst):
    if k == M:
        print(*lst)
        return
    
    for i in range(s, N):
        if used[i] == 0:
            used[i] = 1
            # k : 트리의 깊이, s : 오름차순 수열을 위해 선택한 숫자 뒤의 숫자를 고름 
            backtrack(k + 1, i + 1, lst + [arr[i]])
            used[i] = 0

backtrack(0, 0, [])














