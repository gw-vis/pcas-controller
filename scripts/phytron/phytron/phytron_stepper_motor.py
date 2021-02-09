

import socket
import select
import time
import logging
import logging.config
from .__init__ import get_module_logger

logger = get_module_logger(__name__)

'''
ask_driver_status

1 = Axis busy
2 = Command invalid
4 = Axis waits for synchronisation 8 = Axis initialised
10 = Axis limit switch +
20 = Axis limit switch –
40 = Axis limit switch center
80 = Axis limit switch software +
100 = Axis limit switch software –
200 = Axis power stage is busy
400 = Axis is in the ramp
800 = Axis internal error
1000 = Axis limit switch error
2000 = Axis power stage error
4000 = Axis SFI error
8000 = Axis ENDAT error
10000 = Axis is running
20000 = Axis is in recovery time (s. parameter P13 or P16)
40000 = Axis is in stop current delay time (parameter P43)
80000 = Axis is in position
100000 = Axis APS is ready
200000 = Axis is positioning mode
400000 = Axis is in free running mode
800000 = Axis multi F run
1000000 = Axis SYNC allowed

'''

class controller(object):

    def __init__(self,ipaddr):
        self.ipaddr        = ipaddr
        self.port          = 22222
        self.BUFFER_SIZE = 4096

        #self.reply_message = None

        self.connect()

    def connect(self):

        logger.info('Connecting to {0}:{1}'.format(self.ipaddr,self.port))

        try:
            netAddr=(self.ipaddr, self.port)
            self.netsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.netsock.connect(netAddr)
            self.netsock.setblocking(1)
            self.netsock.settimeout(1.0)

        except socket.error as e:
            logger.info(e)
            print (e)
            print ('Could not connect to {0}:{1}. '\
                'Please check network configuration.'.format(self.ipaddr,self.port))
            print ('exit..')
            exit()

        except Exception as e:

            logger.info(e)
            print (e)
            exit()


    def __enter__(self):
      #self.connect()
      return self

    def read(self):
        time.sleep(0.1)
        try:
            data =  self.netsock.recv(self.BUFFER_SIZE)
            data = data.replace(b'\x02\x06', b'').replace(b'\x03',b'')
          # text = ([chr(ord(i)) for i in data])
          # data = int(''.join(data))
            data =int(data[:-3])
            print(data)

            self.reply_message = data

        except Exception as e:
            logger.warning(e)
            logger.warning('failed data reciving')
            self.reply_message = -1

    def send(self, sendString):

        logger.info('Send "{1}" to {0}'.format(self.ipaddr,sendString))

        try:
            self.netsock.send(sendString)
            
        except socket.error as e:
            logger.info(e)
            logger.info("Reconnecting..")
            self.connect()

        except Exception as e:
            logger.info(e)
            print (type(e))
            print (dir(e))

            logger.info("Exit. Bye")

            exit()

    def close(self):

        logger.info('Closing controller {0}'.format(self.ipaddr))
        self.netsock.close()
        logger.info('OK. Bye {0}'.format(self.ipaddr))

    def __exit__(self,type, value, traceback):
        self.close()

class driver(controller):

    def __init__(self,ipaddr):
        super(driver,self).__init__(ipaddr)
        self.ipaddr = ipaddr
        self.set_resol(1,11)
        #module1と4の分解能を1/128モードに固定。変えない。
        resol = self.netsock.recv(4096)
        #なぜかこの行が無いとモーターが動いてくれない

        #self.set_acc(1,1,500)

    def __enter__(self):
        super(driver,self).__enter__()
        return self


    def reconnect(self):
        self.__init__(self.ipaddr)


    def ask_driver_status(self,ModuleNum):

        self.send(b'\x020SE%d.1:XX\x03'%(ModuleNum))

        error = self.netsock.recv(4096)
        print(hex(int(error[2:9])))

    def ask_position(self,motorAddr):
        
        self.send(b'\x020%d.1P20R:XX\x03'%(int(motorAddr)))

        #position = self.netsock.recv(4096)
        #print(position[2:7])

    def ask_resol(self,motorAddr):

        self.send(b'\x020%d.1P45R:XX\x03'%(motorAddr))

        resol = self.netsock.recv(4096)
        print(resol[2:4])

    def ask_freq(self,motorAddr):

        self.send(b'\x020%d.1P14R:XX\x03'%(motorAddr))

        freq = self.netsock.recv(4096)
        print(freq[2:-4])

    def move_step(self,ModuleNum,count):

        self.send(b'\x020%d.1+%d:XX\x03'%(ModuleNum,count))

        move = self.netsock.recv(4096)
        print(move[1:11])

    def move_stop(self,ModuleNum):

        self.send(b'\x020%d.1S:XX\x03'%(ModuleNum))

        move = self.netsock.recv(4096)
        print(move[1:11])


    def set_resol(self,ModuleNum,resolution):
        self.send(b'\x020%d.1P45S%d:XX\x03'%(ModuleNum, resolution))
        #分解能1/128モードに変える
        
    def set_freq(self,ModuleNum,frequency):
        self.send(b'\x020%d.1P14S%d:XX\x03'%(ModuleNum,frequency))

    def check_error_message(self):
        try:

            logger.info('Reply message is "{0}"'.format(errorMessage[int(self.reply_message)]))

            return errorMessage[int(self.reply_message)]

        except:
            pass
        return -34

    def check_reply_message(self):
        self.read()  
        logger.info('Replay message is "{0}"'.format(self.reply_message))
        return self.reply_message
        
if __name__ == "__main__":
    with driver('10.68.150.63') as k1phy:
          #k1phy.move_step(1,1000)
          k1phy.ask_position(str(1))
          #k1phy.ask_freq(1)
          k1phy.check_reply_message()
          #driver('10.68.150.63').set_freq(1,100)
          #driver('10.68.150.63').set_resol(1,9)
          #driver('10.68.150.63').ask_resol(1)
          #driver('10.68.150.63').ask_driver_status(1)


