N = int(input())
trees = list(map(int, input().split()))
trees.sort()
# print(trees)

def solution(trees):
   # quotient : 몫 
   # remainder : 나머지 
   quoList = [0] * len(trees)
   remList = [0] * len(trees)

   for t in range(len(trees)):
      quoList[t] = trees[t] // 3
      remList[t] = trees[t] % 3

   # print(quoList)
   # print(remList)

   one = remList.count(1)
   two = remList.count(2)
   # 나머지 1과 2의 수가 동일할 경우 -> YES 
   if one == two:
      return 'YES'

   # 나머지 1과 2의 수가 다를 경우
   else:
   #     1이 2보다 많을 때 
      if one > two:
         tmp = one - two
   #     (1의 수 - 2의 수)가 3의 배수일 때,
         if tmp % 3 == 0:
            cnt = tmp // 3
   #     뒤에서부터 for 반복문을 돌아 몫이 1 이상이면 
   #     (1의 수 - 2의 수) - 3 (이 때 반복문을 도는 횟수는 3으로 나눈 몫)
            for i in range(len(remList)-1, -1, -1):
               if remList[i] == 1 and quoList[i] >= 1:
                     cnt -= 1
                     tmp -= 3

               if cnt == 0:
                  break 
            # 남는 나머지 수가 있다면 NO 
            if tmp > 0:
               return 'NO'
            else:
               return 'YES'
         else:
            return 'NO'
         
   #     2가 1보다 많을 때 -> NO
      else:
         return 'NO'

print(solution(trees))


N = int(input())
trees = list(map(int, input().split()))
q = 0
r = 0   

for t in trees:
   q += (t // 2)
   r += (t % 2)
if (q - r) % 3 == 0 and q >= r:
   print('YES')
else:
   print('NO')   







 