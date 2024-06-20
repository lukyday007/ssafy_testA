# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]


# # ver 1
# total = 0
# board = {}
# for r in range(-2000, 2001):
#    for c in range(-2000, 2001):
#       board[(r, c)] = []

# N = int(input())
# for _ in range(N):
#    r, c, d, s = map(int, input().split())
#    r *= 2
#    c *= 2

#    board[(r,c)].append((d,s))


# while N > 0:
#    # 움직임 처리 
#    for k, v in board.items():
#       if board[k]:
#          cr, cc = k
#          print(v)
#          cd, cs = v[0]
#          board[(cr, cc)].remove((cd, cs))

#          nr, nc = cr + dr[cd], cc + dc[cd]
#          if -2000 <= nr <= 2000 and -2000 <= nc <= 2000:
#             if (nr, nc) not in board:
#                board[(nr, nc)] = [(cd, cs)]
#             else:
#                board[(nr, nc)].append((cd, cs))
#          else: # 그냥 소멸
#             pass
   
#    # 충돌 처리 
#    # 서로의 반경 1 거리에 방향ㅇ
#    for k, v in board.items():
#       if len(v) > 1:
#          l = len(v)
#          for i in range(l):
#             total += v[i][1]

#          board[k] = []
#          N -= l

# print(total)
      


# ver 2    

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

# x, y, d, s
# => c, r, d, s
for tc in range(1, int(input()) + 1):
   N = int(input())
   arr = []
   ans = 0
   for _ in range(N):
      c, r, d, s = map(int, input().split())
      c *= 2
      r *= 2
      arr.append([r, c, d, s])

   for _ in range(4001):
      for i in range(len(arr)):
         arr[i][0] += dr[arr[i][2]]
         arr[i][1] += dc[arr[i][2]]
      
      vis, rem = set(), set()
      for j in range(len(arr)):
         cr, cc = arr[j][0], arr[j][1]
         if (cr, cc) in vis:
            rem.add((cr,cc))
         else:
            vis.add((cr, cc))
      
      for k in range(len(arr)-1, -1, -1):
         if (arr[k][0], arr[k][1]) in rem:
            ans += arr[k][3]
            arr.pop(k)
         elif max(abs(arr[k][0]), abs(arr[k][1])) > 2000:
            arr.pop(k)

   print(f'#{tc} {ans}')






