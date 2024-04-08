# 재귀 함수로 접근 

''' 반례- 결과 10
2
5 10
1 10
'''
def resign_recursive(day, total):
   global maxV

   if day > N:
      return
   
   maxV = max(maxV, total)
      
   # if day + T[day + 1] > N:
   if day + 1 <= N:   
      # 선택 o
      resign_recursive(day + T[day + 1], total + P[day + 1])
      # 선택 x
      resign_recursive(day + 1, total)

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
maxV = 0

for i in range(1, N + 1):
   t, p = map(int, input().split())
   T[i] = t
   P[i] = p

resign_recursive(0, 0)
print(maxV)


















