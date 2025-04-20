# multiproc.py
import multiprocessing

def compute_square(num):
    result = num * num
    print(f"{num}:{result}")

if __name__ == "__main__":
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=compute_square, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print("All processes done")