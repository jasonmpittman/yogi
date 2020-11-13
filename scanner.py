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
        for i in range(1, 1024):
            s = socket(AF_INET, SOCK_STREAM)
            if i == 25:
                i += 1
            connection = s.connect_ex((ip, i))
            if connection == 0:
                print("Port ", i,": OPEN", sep='')
            s.close()
        print("Time Taken:", time.time() - startTime)
