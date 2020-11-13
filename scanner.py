__author__ = "Timothy Beal"
__copyright__ = "Copyright 2020"
__credits__ = ["Timothy Beal"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Timothy Beal"
__status__ = "In Development"


from socket import *

import time

startTime = time.time()

class Scanner:
    """
    Runs the scan of the designated ip address and port(s)

    ----------
    Attributes:
    Instantiates Targets() and Detector()
    """
    def scan(ip):
        for i in range(0, 65535):
            s = socket(AF_INET, SOCK_STREAM)

            connection = s.connect_ex((t_IP, i))
            if connection == 0:
                print("Port ", i,": OPEN", sep='')
            s.close()
        print("Time Taken:", time.time() - startTime)
