# ver 1
# def backtrack(k, lst):
#     if k == M:
#         print(*lst)
#         return 
    
#     for i in range(1, N + 1):
#         if lst:
#             if lst[-1] > i:
#                 continue
#         backtrack(k + 1, lst + [i])

N, M = map(int, input().split())
# backtrack(0, [])

# ver 2
def backtrack(k, s, lst):
    if k == M:
        print(*lst)
        return 
    
    for i in range(s, N + 1):
        backtrack(k + 1, i, lst + [i])

backtrack(0, 1, [])
