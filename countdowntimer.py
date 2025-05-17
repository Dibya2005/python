import time
# time.sleep(4)# our program sleep for a given amount of second
# print("h")
t=int(input("enter the time in second : "))
for x in range(t,0,-1):
  sec=x%60
  min=int(x/60)%60
  hour=int(x/3600)

  print(f"{hour:02}:{min:02}:{sec:02}")
  time.sleep(1)
print("time up")