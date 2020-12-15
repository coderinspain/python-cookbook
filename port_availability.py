#Determine port availability
#fint out if a port is already in use
#Different way to do the same task

"""
google - how to find port in use(OS)
$ sudo lsof -i -P -n
$sudo lsof -i -P -n | grep LISTEN
"""

#Imports
import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S',level=logging.DEBUG)

#Check one port
def check_port(ip, port, timeout):
    ret = False
    logging.debug(f'Checking {ip}: {port}')

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.setdefaulttimeout(timeout)
        s.settimeout(timeout)
        con = s.connect_ex(ip, port)
        logging.debug(f'Connection {ip}: {port} = {con}')
        s.close()
        
        if con == 0:
            ret = False
            logging.debug(f'In use {ip}: {port}')
        else:
            ret = True
            logging.debug(f'Usable {ip}: {port}')

    except Exception as ex:
        ret = False
        logging.debug(f'Error {ip}: {port} = {ex.msg}')
    finally:
        logging.debug(f'Returning {ip}: {port} = {ret}')
        return ret

#Checking a range
def check_range(ip, scope):
    ret = {}
    for p in scope:
        r = check_port(ip, p, 1.0)
        ret[p] = r
    return ret


#See it works
def main():
    #Test one port
    port = 3000
    p = check_port('localhost', port, 2.0)
    logging.info(f'Port {port} usable: {p}')

    #Test a range of ports
    ports = check_range('localhost', range(3006, 3500))
    for k, v in ports.items():
        logging.info(f'Port {k} usable {v}')



if __name__ == "__main__":
    main()    