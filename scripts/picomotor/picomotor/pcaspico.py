#
#! coding:utf-8
import os
import pcaspy
import logging
import time
#import config
from . import config
from datetime import datetime
from datetime import timedelta
#import pyttsx
from epics import caget, caput, cainfo

pvdb = config.pvdb
##################################################
#'''

ON = 1.0
#'''
##################################################
#os.environ['EPICS_CAS_INTF_ADDR_LIST'] = '10.68.10.255'
#os.environ['EPICS_CAS_INTF_ADDR_LIST'] = 'localhost'
#os.environ['EPICS_CAS_SERVER_PORT'] = '58901'
# https://pcaspy.readthedocs.org/en/latest/tutorial.html

import logging
import logging.config

#from __init__ import get_module_logger
from .__init__ import get_module_logger
logger = get_module_logger(__name__)
start = 0

target_position = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0
}

class PcasDriver(pcaspy.Driver):
    def __init__(self, driver, prefix):
        super(PcasDriver, self).__init__()
        self.driver = driver
        self.prefix = prefix

        self.logfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/PicoMotor/LogFiles/'+self.prefix+'.log'
  
        driverAddr = 1
        MOTORNUMBER = str(1)
        self.driver.ask_position(driverAddr,MOTORNUMBER)
        pos1 = self.driver.check_reply_message()
        self.setParam(MOTORNUMBER+"_POSITION", pos1)
        caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos1)
        caput(self.prefix+MOTORNUMBER+"_TARGET_POSITION",pos1)
        target_position[MOTORNUMBER]=pos1
        MOTORNUMBER = str(2)
        self.driver.ask_position(driverAddr,MOTORNUMBER)
        pos2 = self.driver.check_reply_message()
        self.setParam(MOTORNUMBER+"_POSITION", pos2)            
        caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos2)
        caput(self.prefix+MOTORNUMBER+"_TARGET_POSITION",pos2)
        target_position[MOTORNUMBER]=pos2
        MOTORNUMBER = str(3)
        self.driver.ask_position(driverAddr,MOTORNUMBER)
        pos3 = self.driver.check_reply_message()
        self.setParam(MOTORNUMBER+"_POSITION", pos3)            
        caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos3)
        caput(self.prefix+MOTORNUMBER+"_TARGET_POSITION",pos3)
        target_position[MOTORNUMBER]=pos3
        MOTORNUMBER = str(4)
        self.driver.ask_position(driverAddr,MOTORNUMBER)
        pos4 = self.driver.check_reply_message()
        self.setParam(MOTORNUMBER+"_POSITION", pos4)            
        caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos4)
        caput(self.prefix+MOTORNUMBER+"_TARGET_POSITION",pos4)
        target_position[MOTORNUMBER]=pos4

        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' initialize actual pos1: '+str(pos1)+' pos2: '+str(pos2)+' pos3: '+str(pos3)+' pos4: '+str(pos4)+'\n')

    def read(self, channel):
        value = self.getParam(channel)    
        return value    
    
    def write(self, channel, value):
        global start
        """
        This function is called every "CAPUT (EPICS-CHANNEL) (VALUE)" command.
        epics_channel : the channlel excluded PREFIX from EPICS-CHANNEL
        value : VALUE
        """
        self.setParam(channel, value) # need ! why????
        driverAddr = 1
        if "REV" in channel and value == ON:
            MOTORNUMBER, OPTION = channel.split("_")
            step = self.getParam(MOTORNUMBER+"_STEP")
            #self.updatePVs()            
            self.driver.move_step(driverAddr,int(MOTORNUMBER),-1*step)
            start = datetime.now()
            target_position[MOTORNUMBER] = target_position[MOTORNUMBER] + -1*step
            caput(self.prefix+MOTORNUMBER+"_TARGET_POSITION",target_position[MOTORNUMBER])

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' channel: '+str(channel)+' REV: '+str(-1*step)+' move to: '+str(target_position[MOTORNUMBER])+'\n')


        if "FWD" in channel and value == ON:
            MOTORNUMBER, OPTION = channel.split("_")
            step = self.getParam(MOTORNUMBER+"_STEP")
            #self.updatePVs()
            self.driver.move_step(driverAddr,int(MOTORNUMBER),step)
            start = datetime.now()
            target_position[MOTORNUMBER] = target_position[MOTORNUMBER] + step
            caput(self.prefix+MOTORNUMBER+"_TARGET_POSITION",target_position[MOTORNUMBER])

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' channel: '+str(channel)+' FWD:'+str(-1*step)+' move to: '+str(target_position[MOTORNUMBER])+'\n')

        if "COMMAND" in channel:
            command = value
            #print command
            self.driver.send(command)            
        if "STATUS" in channel and value == ON:
            #self.setParam("ERRORMESSAGE", 'Please Wait!')
            #self.updatePVs()
            #time.sleep(1)
            MOTORNUMBER = str(1)
            self.driver.ask_position(driverAddr,MOTORNUMBER)
            pos1 = self.driver.check_reply_message()
            self.setParam(MOTORNUMBER+"_POSITION", pos1)
            caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos1)
            MOTORNUMBER = str(2)
            self.driver.ask_position(driverAddr,MOTORNUMBER)
            pos2 = self.driver.check_reply_message()
            self.setParam(MOTORNUMBER+"_POSITION", pos2)            
            caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos2)
            MOTORNUMBER = str(3)
            self.driver.ask_position(driverAddr,MOTORNUMBER)
            pos3 = self.driver.check_reply_message()
            self.setParam(MOTORNUMBER+"_POSITION", pos3)            
            caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos3)
            MOTORNUMBER = str(4)
            self.driver.ask_position(driverAddr,MOTORNUMBER)
            pos4 = self.driver.check_reply_message()
            self.setParam(MOTORNUMBER+"_POSITION", pos4)            
            caput(self.prefix+MOTORNUMBER+"_ACTUAL_POSITION",pos4)

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' status actual pos1: '+str(pos1)+' pos2: '+str(pos2)+' pos3: '+str(pos3)+' pos4: '+str(pos4)+'\n')
            #
            self.driver.ask_driver_error()
            error = self.driver.check_reply_message()
            self.setParam("ERROR", error)
            errormessage = self.driver.check_error_message()
            self.setParam("ERRORMESSAGE", errormessage)
            #self.setParam("ERRORMESSAGE", 'hoge')
            start = datetime.now()

            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' status error: '+str(error)+' errormessage: '+errormessage+'\n')
             
        self.updatePVs()
        return True
    
class PcasServer(pcaspy.SimpleServer):
    def __init__(self, prefix, driver):
        super(PcasServer, self).__init__()
        logger.info("Initialize PCAServer")
        self.server = pcaspy.SimpleServer()
        self.server.createPV(prefix, pvdb)
        self.driver = driver
        driver_ = PcasDriver(driver,prefix)
        
    def run(self):
        global start

        logger.info("Start server.")        
        i = 0
        start = datetime.now()
        dt = timedelta(seconds=3600)
        while True:
            self.server.process(0.1)
            now = datetime.now()
            diff = now- start
            #print diff,dt,diff>dt
            if diff>dt: # 12sec
                d = datetime.now()
                with open(self.logfile,'a') as f:
                    f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' Script Time out:'+str(diff)+'\n')
                self.driver.close()
                print("==================================")
                print('60 minutes passed. Bye!')
                print("I'll be back..")
                print("""
                　　　　　　　　　　　 /j^i
                　　　　　　　　　　 ./　 ;!
                　　　　　　　　　　/　 /_＿,,..
                　　　　　　　　　/　　`(_t＿,__〕
                　　　　　　　　 /　　　 '(_t＿,__〕
                　　　　　　　　/　　　　｛_i＿,__〕
                　　　　　　 ／　　　 ノ　 {_i＿_〉
                　　　　　／　　　　　　＿,..-'"
                　　　／　　　　　　／
                ～～～～～～～～～～～～～～～～
                """)
                print("==================================")
                #engine = pyttsx.init()
                #engine.setProperty('rate', 100)
                #engine.say('Bye')
                #engine.runAndWait()
                exit()
            else:
                i=i+1

if __name__ == '__main__':
    import pcaspico
    import newfocus8742
    import sys
    import time
    #import subprocess
    #pl = subprocess.Popen('ps -ef | grep python',shell=True,stdout=subprocess.PIPE).communicate()[0]
    #print(pl)
    #exit()
    prefix   = 'K1:PICO-TEST_'
    driverIP = '10.68.150.44'
    mydriver   = newfocus8742.driver(driverIP)
    picoserver = pcaspico.PcasServer(prefix, mydriver)
    try:
        picoserver.run()
    except KeyboardInterrupt as e:
        mydriver.close()
        print(e)
        print('Detect keyboard interrupt. Bye!')
        exit()
