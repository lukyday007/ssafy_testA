# N : 줄의 개수 
# 숫자 배열 
# 덧셈, 뺄셈, 곱셈, 나눗셈 
# ver 1 
# def calculate(nums, ops):
#    st = [nums[0]]
#    for i in range(len(ops)):
#       if ops[i] == '+':
#          tmp = st.pop()
#          st.append(tmp + nums[i + 1]) 
#       elif ops[i] == '-':
#          tmp = st.pop()
#          st.append(tmp - nums[i + 1]) 
#       elif ops[i] == '*':
#          tmp = st.pop()
#          st.append(tmp * nums[i + 1]) 
#       else:
#          '''
#          a, b = -6, 3
#          tmp = a*(-1)//b
#          restmp = (-1)*tmp
#          print(restmp)

#          '''
#          tmp = st.pop()
#          if tmp < 0:
#             res = tmp*(-1) // nums[i + 1]
#             res = (-1)*res
#             st.append(res)
#             continue
#          st.append(tmp // nums[i + 1]) 

#    return st[-1]

# def dfs(k):
#    global minV, maxV

#    if k == M:
#       lst = operator[:]        
#       res = calculate(arr, lst)
#       minV = min(res, minV)
#       maxV = max(res, maxV)
#       return 

#    # 교환
#    for i in range(k, M):
#       operator[k], operator[i] = operator[i], operator[k]
#       dfs(k + 1)
#       operator[k], operator[i] = operator[i], operator[k]


# N = int(input())
# arr = list(map(int, input().split()))
# op = list(map(int, input().split()))
# M = sum(op)
# operator = []
# for o in range(len(op)):
#    if o == 0:
#       for _ in range(op[o]):
#          operator.append("+")
#    elif o == 1:
#       for _ in range(op[o]):
#          operator.append("-")
   
#    elif o == 2:
#       for _ in range(op[o]):
#          operator.append("*")

#    else:
#       for _ in range(op[o]):
#          operator.append("//")

# minV = 0xfffffff
# maxV = 0

# dfs(0)
# print(maxV)
# print(minV)


# ver 2 
# def backtrack(k, a, s, m, d, total):
#    global minV, maxV
   
#    if k == N:
#       minV = min(minV, total)
#       maxV = max(maxV, total)
#       return 

#    if a > 0:
#       backtrack(k + 1, a - 1, s, m, d, total + arr[k])
#    elif s > 0:
#       backtrack(k + 1, a, s - 1, m, d, total - arr[k])
#    elif m > 0:
#       backtrack(k + 1, a, s, m - 1, d, total * arr[k])
#    else:
#       if total < 0:
#          res = total*(-1) // arr[k]
#          res = (-1) * res
#          backtrack(k + 1, a, s, m, d - 1, res)
#       else:
#          backtrack(k + 1, a, s, m, d - 1, total // arr[k])

# N = int(input())
# arr = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())

# # -10억 보다는 크거나 같고, 10억보다는 작거나 같다 
# minV = 1e10
# maxV = -1e10
# backtrack(1, add, sub, mul, div, arr[0])
# print(maxV)
# print(minV)



# ver 3: if, elif, else로 쓰면 순열 구조가 안됨! 오직 수직으로만 진행되기 때문!
def backtrack(k, a, s, m, d, total):
   global minV, maxV
   # 가지치기 : 속도가 조금 빨라짐 
   if total < int(-1e10) or total > int(1e10):
      return 
   
   if k == N:
      minV = min(minV, total)
      maxV = max(maxV, total)
      return 

   if a > 0:
      backtrack(k + 1, a - 1, s, m, d, total + arr[k])
   if s > 0:
      backtrack(k + 1, a, s - 1, m, d, total - arr[k])
   if m > 0:
      backtrack(k + 1, a, s, m - 1, d, total * arr[k])
   if d > 0:
      if total < 0:
         res = total*(-1) // arr[k]
         res = (-1) * res
         backtrack(k + 1, a, s, m, d - 1, res)
      else:
         backtrack(k + 1, a, s, m, d - 1, total // arr[k])

N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# -10억 보다는 크거나 같고, 10억보다는 작거나 같다 
minV = int(1e10)
maxV = int(-1e10)
backtrack(1, add, sub, mul, div, arr[0])
print(maxV)
print(minV)





























