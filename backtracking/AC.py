# 뒤집기 R
# 버리기 D ( 첫 번째 수 )
# T : 테스트 케이스의 수, p : 수행할 함수, n : 배열의 개수
# ver 1 
# from collections import deque

# def solution():
#    if len(p) > n:
#       return 'error'
   
#    right = False
#    idx = 0
#    while idx + 1 <= len(p) :
#       if p[idx] == "D"and not right:
#          Q.popleft()
#       elif p[idx] == "D" and right:
#          Q.pop()
#       elif p[idx] == "R" and not right :
#          right = True
#       elif p[idx] == "R" and right:
#          right = False 
#       idx += 1 
   
#    if right:
#       Q.reverse()

#    return Q

# for _ in range(int(input())):
#    p = list(input())
#    n = int(input())
#    a = input()
#    Q = deque()
#    for i in range(len(a)):
#       if a[i] != '[' and a[i] != ']' and a[i] != ",":
#          Q.append(int(a[i]))

#    res = solution()
#    if res != 'error':
#       print('['+','.join(map(str,res))+']')
#    else:
#       print('error')


# ver 2
from collections import deque

def solution():
   if not n:
      # 숫자가 없을 때 뒤집기는 빈 리스트 [] 출력 
      if "D" in p:
         return 'error'
      # 숫자가 없을 때 삭제는 에러 
      else:
         return '[]'
   else:
      # 명령어가 숫자보다 많으면 에러 
      if p.count("D") > n:
         return 'error'
      
   right = False
   idx = 0
   while idx + 1 <= len(p) :
      if p[idx] == "D"and not right:
         Q.popleft()
      elif p[idx] == "D" and right:
         Q.pop()
      elif p[idx] == "R" and not right :
         right = True
      elif p[idx] == "R" and right:
         right = False 
      idx += 1 

   if right:
      Q.reverse()

   return Q

for _ in range(int(input())):
   p = list(input())
   n = int(input())
   Q = deque(input()[1:-1].split(','))

   if n == 0:
      Q = deque()

   res = solution()
   if res == 'error':
      print('error')
   elif res == '[]':
      print('[]')
   else:
      print('['+','.join(map(str,res))+']')





