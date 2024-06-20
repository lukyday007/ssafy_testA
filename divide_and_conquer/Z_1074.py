# # ver 1, 2 
# def solve(sr, er, sc, ec):
#    global idx, r, c 

#    if sr + 1 == er and sc + 1 == ec:
#       if sr == r and sc == c:
#          print(idx)
#          exit()
#       idx += 1 
#       return 

#    mr = (sr + er)//2
#    mc = (sc + ec)//2

#    solve(sr, mr, sc, mc)
#    solve(sr, mr, mc, ec)
#    solve(mr, er, sc, mc)
#    solve(mr, er, mc, ec)

# idx = 0 
# N, r, c = map(int, input().split())
# N = 2 ** N
# solve(0, N, 0, N)

# # for b in board:
# #    print(*b)
# # print()


# ver 3
def solve(N, r, c):
   ans = 0
   cr, cc = 2 ** N, 2 ** N
   part = (2 ** N) * (2 ** N)
   
   while N >= 0:

      if r < cr and c < cc:    # 위, 왼쪽
         cr -= int(2 ** (N-1)) 
         cc -= int(2 ** (N-1))  
         print(1)
         print(cr, cc, part, ans )

      elif r < cr and c >= cc: # 위, 오른쪽
         cr -= int(2 ** (N-1)) 
         cc += int(2 ** (N-1))
         ans += (1 * part) 
         print(2)
         print(cr, cc, part, ans )

      elif r >= cr and c < cc: # 아래, 왼쪽
         cr += int(2 ** (N-1)) 
         cc -= int(2 ** (N-1)) 
         ans += (2 * part)
         print(3)
         print(cr, cc, part, ans )

      else:                    # 아래, 오른쪽
         cr += int(2 ** (N-1)) 
         cc += int(2 ** (N-1))
         ans += (3 * part)
         print(4)
         print(cr, cc, part, ans )

      part //= 4
      N -= 1

   print(ans)

N, r, c = map(int, input().split())
solve(N, r, c)



