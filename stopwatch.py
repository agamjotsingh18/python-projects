# from time import *
# import threading
# timee=0
# print('STOPWATCH ')
# print("WELCOME")
# input("press ENTER to start stopwatch and press CTRL-C key to stop")
# #while True:
   
# try:
#     print("STOPWATCH STARTED")
    
#     while True:
#         timee+=1
            
#         print("Time elapsed is",timee," seconds")
#         sleep(1)
# except KeyboardInterrupt:
        
#     print("stopwatch stopped")

# print("total time is",timee,"seconds")

#********************************************************************************************************
import time

print('STOPWATCH ')
print("WELCOME")
while True:
    try:
        input("press ENTER to start stopwatch and press CTRL-C key to stop")
        start_time=time.time()
        print("STOPWATCH STARTED")     
        while True:              
            print("Time elapsed is",round(time.time()-start_time,0)," seconds \n")
            time.sleep(1)
            
    except KeyboardInterrupt:
            
        print("stopwatch stopped")
        end_time=time.time()
        print("Time elapsed is",round(end_time-start_time,2)," seconds ")
        break


