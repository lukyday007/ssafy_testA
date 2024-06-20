# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

# 백트레킹 - 완탐으로 풀기 
def solution(N, cnt):
   global minV 

   if N == 1:
      minV = min(cnt, minV)
      return 
   
   solution(N - 1, cnt + 1)
   if N % 3 == 0:
      solution(N / 3 , cnt + 1)
   if N % 2 == 0:
      solution(N / 2, cnt + 1)


# N = int(input())
# minV = 1e6
# solution(N, 0)            
# print(minV)


# dp로 풀기 




N = int(input())
D = [0] * (N + 1)
D[1] = 0

for i in range(2, N + 1):

   D[i] = D[i-1] + 1
   if i % 2 == 0:
      D[i] = min(D[i], D[i // 2] + 1)
   if i % 3 == 0:
      D[i] = min(D[i], D[i // 3] + 1)

# print(D)
print(D[N])

