__author__ = "Timothy Beal"
__copyright__ = "Copyright 2020"
__credits__ = ["Timothy Beal"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Timothy Beal"
__status__ = "In Development"


from scapy.all import *

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import random

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
        port_rng=[22,23,80,443]
        for dst_p in port_rng:
            src_p = random.randint(1024,65534)
            resp = sr1(
                IP (dst=ip) / TCP (sport = src_p, dport = dst_p,
                flags = "S"), timeout=1, verbose = 0)
            if resp is None:
                print(f"{ip}:{dst_p} is filtered.")

            elif resp.haslayer(TCP):
                if resp.getlayer(TCP).flags == 0x12:
                    send_rst = sr(
                        IP (dst=ip) / TCP (sport = src_p, dport = dst_p,
                        flags='R'), timeout = 1, verbose = 0)
                    print(f"{ip}:{dst_p} is open.")
            elif resp.getlayer(TCP).flags == 0x14:
                print(f"{ip}:{dst_p} is closed.")

            elif resp.haslayer(ICMP):
                if(
                    int(resp.getlayer(ICMP).type) == 3 and
                    int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
                ):
                    print(f"{ip}:{dst_p} is filtered.")


        print("Time Taken:", time.time() - startTime)
