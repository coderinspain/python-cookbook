# Thread Locking
#Avoiding the dreaded race conditions and deadlocks
#Race condition: same resource modified by multiple threads
#Deadlock: multiple threads waiting on the same resource


#Imports
import logging
import threading
from concurrent.futures import ThreadPoolExecutor #This is Python 3.2 >
import time
import random

counter = 0

#Test function
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')

    for x in range(count):
        logging.info(f'Count: {threadname} += {count}')

    #Locking
    # lock = threading.Lock()
    # lock.acquire()
    # lock.acquire()
    # try:
    #     counter += 1
    # finally:
    #     lock.release()
    
    #Locking Simplified
    lock = threading.Lock()
    with lock:
        logging.info(f'Locked: {threadname}')
        counter += 1
        time.sleep(2)


    logging.info(f'Completed: {threadname}')


#Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S',level=logging.DEBUG)
    logging.info('App Start')

    workers = 5
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1, 5)
            ex.submit(test, v)

    logging.info(f'Counter: {counter}')
    logging.info('App Finished')


if __name__ == "__main__":
    main()