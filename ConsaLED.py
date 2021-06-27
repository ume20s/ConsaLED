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
time.sleep(0.4)
pi.digitalWrite( LED, 0 )

def word(recv_data):
    for line in recv_data.split('\n'):
        index1 = line.find('WORD="')
        index2 = line.find('CM="')
        if index1!=-1:
            WORD = line[index1+6:line.find('"',index1+6)]
            if index2!=-1:
                CM = float(line[index2+4:line.find('"',index2+4)])
                if(WORD!='[s]' and WORD!='[/s]'):
                    if WORD == 'CONSA' and CM >= 0.9:
                        print(CM)
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
                    yield WORD

def main():
    host = 'localhost'
    port = 10500

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        data = ''
        while 1:
            if '\n.' in data:
                data = data[data.find(''):].replace('\n.', '')
                print(''.join(word(data)))
                data = ''
            else:
                data = data + client.recv(1024).decode('utf-8')
    except KeyboardInterrupt:
        client.close()

if __name__ == "__main__":
    main()
