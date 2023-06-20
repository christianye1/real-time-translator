import time
now = time.time()
while True:
    elapsed_time = int(time.time())- int(now)
    print("elapsed time: "+ str(elapsed_time))