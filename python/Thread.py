import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)

# Normal Code
time1 = time.time()
func(4)
func(2)
func(1)
time2 = time.time()
print(f"Normal code execution time: {time2 - time1} seconds")
# Now i can start all the functions in parallel using threading.
 
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

time1 = time.time()
t1.start()
t2.start()
t3.start()
time2 = time.time() 
print(f"Threaded code execution time: {time2 - time1} seconds")

# .join() method is used to wait for the thread to complete its execution before moving on to the next line of code.
# starting the threads again to see the difference in execution time with .join() method.
# thread can only be started once, so we need to create new threads for the same function.
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
time1 = time.time()
t1.start()
t2.start()
t3.start()
t1.join()   
t2.join()     
t3.join()     
time2 = time.time()
print(f"Threaded code execution time with .join(): {time2 - time1} seconds")