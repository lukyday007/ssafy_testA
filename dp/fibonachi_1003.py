for _ in range(int(input())):
   N = int(input())
   zero = [0] * (N + 1)
   one = [0] * (N + 1)

   for i in range(N + 1):
      if i == 0:
         zero[i] = 1
      elif i == 1:
         one[i] = 1
      else:
         zero[i] = zero[i - 2] + zero[i - 1]
         one[i] = one[i - 2] + one[i - 1]

   print(zero[N], one[N])










