# 중복 순열, 완탐, 시뮬레이션, dfs

# def backtrack(n, a, s, m, d, total):
#    global minV, maxV 

#    if total <= int(-1e9) or int(1e9) <= total:
#       return

#    if n == N:
#       minV = min(total, minV)
#       maxV = max(total, maxV)
#       return 
   
#    if a > 0:
#       backtrack(n + 1, a - 1, s, m, d, total + nums[n])
#    if s > 0:
#       backtrack(n + 1, a, s - 1, m, d, total - nums[n])
#    if m > 0:
#       backtrack(n + 1, a, s, m - 1, d, total * nums[n])
#    if d > 0:
#       backtrack(n + 1, a, s, m, d - 1, int(total / nums[n]))

# for tc in range(1, int(input()) + 1):
#    N = int(input())
#    add, sub, mul, div = map(int, input().split())
#    nums = list(map(int, input().split()))
#    maxV, minV = float('-inf'), float('inf')
#    backtrack(1, add, sub, mul, div, nums[0])
#    print(f"#{tc} {maxV - minV}")



'''
1
5
2 1 0 1
3 5 3 7 9

24
'''

# def backtrack(k, total):
#    global minV, maxV

#    if k == N:
#       minV = min(minV, total)
#       maxV = max(maxV, total)
#       return
   
#    for i in range(4):   # 연산자 리스트 길이는 항상 4
#       if not op[i]: continue
#       op[i] -= 1
#       if i == 0:  # 덧셈일 때 
#          backtrack(k + 1, total + nums[k])
#       if i == 1:  # 뺄셈일 때 
#          backtrack(k + 1, total - nums[k])
#       if i == 2:  # 곱셈일 때 
#          backtrack(k + 1, total * nums[k])
#       if i == 3:  # 나눗셈일 때  
#          backtrack(k + 1, int(total / nums[k]))
#       op[i] += 1

# for tc in range(1, int(input()) + 1):
#    N = int(input())
#    op = list(map(int, input().split()))
#    nums = list(map(int, input().split()))
#    maxV, minV = int(-1e8), int(1e8)
#    backtrack(1, nums[0])   # index, total 
#    print(f"#{tc} {maxV - minV}")

'''
4
123 1 1
356 1 0
327 2 0
489 0 1
'''

from itertools import permutations
N = int(input())

numbers = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))
L = len(numbers)

for _ in range(N):
   number, strike, ball = map(int, input().split())
   number = list(str(number))

   idx = 0
   possibility = 0
   while idx < len(numbers):
      s, b = 0, 0

      for i in range(3):   # 일, 십, 백의 자리 수 
         if number[i] == numbers[idx][i]:
            s += 1
         elif number[i] in numbers[idx]:
            b += 1
   
      if strike == s and ball == b:
         possibility += 1

      if s != strike or b != ball:
         numbers[idx], numbers[len(numbers)-1] = numbers[len(numbers)-1], numbers[idx]
         numbers.pop()
      
      if possibility == N:
         idx += 1
         possibility = 0
         
print(len(numbers))
