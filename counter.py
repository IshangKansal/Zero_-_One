# import time

# def countdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         time_sec -= 1

#     print("stop")

# countdown(5)

import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))

z = input()
