
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:21:12 2021

@author: Brendon
"""

import io
import socket
import struct
import time
import picamera
import fcntl
import  sys
import threading
from Motor import *
from servo import *
from Led import *
from Buzzer import *
from ADC import *
from Thread import *
from threading import Timer
from threading import Thread
from Command import COMMAND as cmd

class Server:
    def __init__(self):
        self.PWM=Motor()
        self.servo=Servo()
        self.led=Led()
        self.buzzer=Buzzer()
        self.adc=Adc()
        self.tcp_Flag = True
        self.sonic=False
        self.Light=False
        self.Mode = 'one'
        self.endChar='\n'
        self.intervalChar='#'
    def get_interface_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                            0x8915,
                                            struct.pack('256s',b'wlan0'[:15])
                                            )[20:24])
    def StartTcpServer(self):
        HOST=str(self.get_interface_ip())
        self.server_socket1 = socket.socket()
                                                