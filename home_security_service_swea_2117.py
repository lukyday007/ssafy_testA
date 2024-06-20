# 홈 방법 서비스 
# 도시 크기 N, 집당 지불 비용 M
# # ver 1 
# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
# maxV = 0

# '''
# 8 3
# 0 0 0 0 0 1 0 0
# 0 1 0 1 0 0 0 1
# 0 0 0 0 0 0 0 0
# 0 0 0 1 0 1 0 0
# 0 0 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 1 0
# 1 0 0 0 0 0 0 0

# 5
# '''
# for r in range(N):
#    for c in range(N):
#       for k in range(1, N + 2):
#          # 비용 계산 
#          cost = k * k + (k - 1) * (k - 1)
#          home = 0
#          q = 0
#          for i in range(r + k):
#             for j in range(c + (k // 2) - q, c + (k // 2) + q + 1):
#                if q < (k // 2):
#                   q += 1
#                else:
#                   q -= 1
#                # 인덱스 에러 방지 
#                if i < 0 or i >= N or j < 0 or j >= N:
#                   continue
#                if city[i][j]:
#                   home += 1
#          # print(i, j)
#          # print(home * M, cost)
#          if home * M > cost:
#             if home*M == 12 and cost == 5:
#                print(f"c: {c}, r: {r}, k: {k}, home: {home}, cost: {cost}, {i}, {j}")
#             # print('이득이 더 큼!')
#             # maxV = max(maxV, (home * M - cost))

# print(maxV)

'''
1
7 7
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 0 0 0
'''

# # ver 2
# for tc in range(1, int(input()) + 1):
#    N, M = map(int, input().split())
#    city = [list(map(int, input().split())) for _ in range(N)]
#    maxV = 0

#    for r in range(N):
#       for c in range(N):
#          for s in range(1, N*2):
#             house = 0
#             for i in range(r - s + 1, r + s):
#                for j in range(c - s + 1 + abs(i - r), c + s - abs(i - r)):
#                   # 범위 넘어가지 않게 
#                   if 0 <= i < N and 0 <= j < N:
#                      if city[i][j]:
#                         house += 1

#             cost = s * s + (s - 1) * (s - 1)
#             if house * M >= cost:               
#                maxV = max(house, maxV)

#    print(f"#{tc} {maxV}")


# ver 3
def solve():
   maxV = 0
   house = [(r, c) for r in range(N) for c in range(N) if city[r][c]]

   for r in range(N):
      for c in range(N):
         dist = [0] * 40
         for cr, cc in house:
            # 거리 계산 주의! 0 -> 길이 1 
            d = abs(r - cr) + abs(c - cc) + 1
            dist[d] += 1
         
         cnt = 0
         for s in range(1, N + 2):
            cnt += dist[s]
            if cnt * M >= cost[s] and maxV < cnt:
               maxV = cnt 

   return maxV

for tc in range(1, int(input()) + 1):
   N, M = map(int, input().split())
   city = [list(map(int, input().split())) for _ in range(N)]
   cost = [k*k + (k-1)*(k-1) for k in range(N + 2)]

   print(f"#{tc} {solve()}")

















