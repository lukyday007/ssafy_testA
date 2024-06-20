from collections import deque
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
for i in range(len(belt)):
   belt[i] = [0, belt[i]]

print(belt)

# deque로 접근 
def work(Q, K):
   step = 1
   zero = 0
   while zero < K + 1:
      if belt.count(0) >= K:
         return step

      robot, val = Q.popleft()
      if val > 0:
         if val - 1 == 0:
            zero += 1
         Q.appendleft([1, val - 1])
         
      robot, val = Q.pop(N//2 - 1)
      if robot == 1:
         step += 1
      Q.insert(N//2 - 1, [0, val])


print(work(belt, K))
   
         













