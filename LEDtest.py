#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import sys
import time
import wiringpi as pi

LED = 4

pi.wiringPiSetupGpio()
pi.pinMode( LED, 1 )

pi.digitalWrite( LED, 1 )
time.sleep(0.1)
pi.digitalWrite( LED, 0 )
time.sleep(0.1)
pi.digitalWrite( LED, 1 )
time.sleep(0.1)
pi.digitalWrite( LED, 0 )
time.sleep(0.3)
pi.digitalWrite( LED, 1 )
time.sleep(0.1)
pi.digitalWrite( LED, 0 )
time.sleep(0.15)
pi.digitalWrite( LED, 1 )
time.sleep(0.1)
pi.digitalWrite( LED, 0 )
time.sleep(0.3)
pi.digitalWrite( LED, 1 )
time.sleep(0.1)
pi.digitalWrite( LED, 0 )
time.sleep(0.3)

