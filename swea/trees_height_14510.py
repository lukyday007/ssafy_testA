tmp1 = []
tmp2 = []

# for _ in range(50):
#    ans = list(input().split())
#    tmp2.append(int(ans[1]))

for tc in range(1, int(input()) + 1):
   N = int(input())
   trees = list(map(int, input().split()))
   height = max(trees)
   # 가장 높은 높이의 나무가 하나만 있지 않을 경우 
   cnt = trees.count(height)
   while cnt > 0:
      trees.remove(height)
      cnt -= 1

   days = 0

   d = 0    # 2로 나눈 몫
   r = 0    # 2로 나눈 나머지 
   for tree in trees:
      tree = height - tree
      d += (tree // 2)
      r += (tree % 2)
   print(trees)
   # print(trees)
   # print(d, r)

   if d > r:
      d -= r
      days += (r * 2)
      tmp = d * 2
      d = tmp // 3
      r = tmp % 3
      days += (d * 2 + r)

   else:
      print(d, r)
      print(f"나머지가 큰 경우")
      r -= d
      days += (d * 2)
      # if r % 2 == 0:
      #    tmp = 2 * r
      # else:
      #    tmp = 2*r - 1
      # days += tmp
      d = r // 3
      r = r % 3
      days += (d * 2 + r)
   print(f'#{tc} {days}')

# for i in range(50):
#    if tmp1[i] != tmp2[i]:
#       print(i + 1)









