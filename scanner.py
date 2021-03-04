#!/usr/bin/python3

__author__ = "Timothy Beal"
__copyright__ = "Copyright 2020"
__credits__ = ["Timothy Beal"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Timothy Beal"
__status__ = "In Development"

import subprocess

import os

class Scanner:
    """
    Runs the scan of the designated ip address and port(s)

    ----------
    Attributes:
    ip: string
    target_info: dictionary
    """
    def scan(ip):
    """
    Calls a sub process to nmap with OS detection enabled 
    and stored the output in target_info

    ----------
    Parameter:
    ip: int
    """
        test = False
        output = subprocess.check_output(["sudo", "nmap", "-O", "-oN", "temp.txt", ip])
        inFile = open('temp.txt', 'r')

        while test is False:
            line = inFile.readline()
            if line[0] == 'R':
                test=True
                print(line)
           
        test = line.split(': ')
        print(test[1])
        test2 = test[1].split(', ')
        print(test2[0])
        print(test2[1])
        print(test2[2])
