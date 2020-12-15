# UDP_Sockets
#UDP does not have concepts like connections, clients, servers
#Think of UDP as anyone can shout out at any time

"""
UDP (User Datagram Protocol) is a communictions protocol
that is primarily used for establishing low-latency and loss-toleratin connections between applications on 
the internet.
It sppeds up transmissions by enabling the transfer of data before an agreement is provided by the receiving party.

"""
#Imports
import logging
import multiprocessing
import threading
import socket
import sys
import time

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S',level=logging.DEBUG)

#Socket
def make_socket(ip='localhost', port=4450, sender=False):
    proc = multiprocessing.current_process().name
    logging.info(f'{proc}: starting')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sender:
        logging.info(f'{proc}: starting to send')
    else:
        logging.info(f'{proc}: binding to port')
        address = (ip, port)
        s.bind(address)

    with s:         
        address = (ip, port)
        s.connect(address)
        while True:
            if sender:
                logging.info(f'{proc}: sending....')
                s.sendto(b'Hello UDP', address)
                time.sleep(1)
            else:
                data, addr = s.recvfrom(1024)
                logging.info(f'{proc}: from {addr} = {data}')

#see in action
def main():
    broadcaster = multiprocessing.Process(target=make_socket, kwargs={'sender':True}, daemon=True, name='Brocaster')
    listener = multiprocessing.Process(target=make_socket, kwargs={'sender':False}, daemon=True, name='Listener')

    broadcaster.start()
    listener.start()

    timer = threading.Timer(5, sys.exit, [0])
    timer.start()


if __name__ == "__main__":
    main()
