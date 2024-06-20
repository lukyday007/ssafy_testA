# ver 1 
N = int(input())
res = [0] * ( N + 1 )     # N 자리의 이친수 개수 
res[0] = 0
res[1] = 1

if N >= 2:
   idx = 2
   while idx < N + 1:
      res[idx] = res[idx - 1] + res[idx - 2]
      idx += 1

print(res[N])
      
# # ver 2 
# N = int(input())
# D = [[0 for j in range(2)] for i in range(N + 1)]
# D[1][1] = 1
# D[1][0] = 0

# for i in range(2, N + 1):
#    D[i][0] = D[i-1][0] + D[i-1][1]
#    D[i][1] = D[i-1][0]

# # for d in D:
# #    print(*d, sum(d))
# # print() 
# print(D[N][0] + D[N][1])



















