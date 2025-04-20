from multiprocessing import Queue,Process
import time
def producer(q):
    for i in range(3):
        q.put(i)
        time.sleep(0.5)

def consumer(q):
    for i in range(3):
        item=q.get()
        print(item)
        time.sleep(1)

if __name__=="__main__":
    q=Queue()
    prod=Process(target=producer, args=(q,))
    cons=Process(target=consumer, args=(q,))
    prod.start()
    cons.start()
    prod.join()
    cons.terminate()