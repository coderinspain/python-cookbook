#Multiprocessing Pool

#Pools of processes and their results


#Imports
import logging
import multiprocessing
from multiprocessing.context import Process
import time
import random


#Worker process
def work(item, count):
    name = multiprocessing.current_process().name
    logging.info(f'{name} Started: {item}')
    for x in range(count):
        logging.info(f'{name} {item} = {x}')
        time.sleep(1)
    logging.info(f'{name} Finished')
    return item + ' is finished'

#Main process

def proc_result(result):
    logging.info(f' Result: {result} ')
    

def main():

    logging.info('Started')

    max = 5
    pool = multiprocessing.Pool(max) 
    results = []
    for x in range(max):
        item = 'Item' + str(x)
        count = random.randrange(1, 10)
        r = pool.apply_async(work, [item, count], callback=proc_result)
        results.append(r)

    #Wait for the process 
    for r in results:
        r.wait()

    #pool.close or pool.terminate
    pool.close()
    pool.join()
    logging.info('Finished')


logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S',level=logging.DEBUG)
if __name__ == "__main__":
    main()
