import threading

def task(name):
    for i in range(3):
        print(f"{name}:{i}")

t1=threading.Thread(target=task, args=("Thread-1",))
t2=threading.Thread(target=task, args=("Thread-2",))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done")


# Thread-1:0 Thread-2:0 Shows thread 1 and 2 are executing the first print statement almost simultaneously

# Thread-1:1
# Thread-1:2
# Thread-2:1
# Thread-2:2
# Done