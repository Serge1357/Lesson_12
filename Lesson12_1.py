import time
import concurrent.futures

def fact(a):
    k = 1
    for i in range(1, a + 1):
        k = k * i
    return k

if __name__ == '__main__':
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(fact, i) for i in [5, 8, 3, 4, 6]]
        results1 = [future.result() for future in concurrent.futures.as_completed(futures)]

    time1 = time.time()-start_time

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(fact, i) for i in [5, 8, 3, 4, 6]]
        results2 = [future.result() for future in concurrent.futures.as_completed(futures)]

    time2 = time.time()-start_time

    if time1 < time2:
        print("ThreadPoolExecutor:",results1, time1)
    else:
        print("ProcessPoolExecutor:",results2, time2)
