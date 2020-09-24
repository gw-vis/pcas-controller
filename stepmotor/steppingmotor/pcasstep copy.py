#!/usr/bin/env python

import os
import pcaspy
#import conf
import logging
from datetime import datetime
from multiprocessing import Process, Value, Array
import time

##################################################

pvdb ={
    '0_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '0_ACC': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '0_VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '0_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '0_POSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '0_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '0_RIGHTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '0_LEFTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '0_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '0_ERROR': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_ACC': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '1_VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '1_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_POSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_RIGHTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_LEFTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '1_ERROR': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_ACC': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '2_VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '2_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_POSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_RIGHTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_LEFTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '2_ERROR': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_ACC': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '3_VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '3_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_POSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_RIGHTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_LEFTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '3_ERROR': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_ACC': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '4_VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '4_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_POSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_RIGHTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_LEFTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '4_ERROR': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_ACC': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '5_VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    '5_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_POSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_RIGHTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_LEFTLIMITSWITCHSTATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    '5_ERROR': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    }
}

##################################################

#os.environ['EPICS_CAS_INTF_ADDR_LIST'] = 'localhost'
#os.environ['EPICS_CAS_SERVER_PORT'] = '58901'

# https://pcaspy.readthedocs.org/en/latest/tutorial.html

class PcasDriver(pcaspy.Driver):
    def __init__(self, driver, prefix):
        super(PcasDriver, self).__init__()
        self.driver = driver
        #self.conf = conf
        self.prefix = prefix
        print driver
        print prefix
        self.driver.setTargetSpeed(500, 0)
        self.driver.setAcceleration(500,0)
        self.driver.setTargetSpeed(500, 1)
        self.driver.setAcceleration(500,1)
        self.driver.setTargetSpeed(500, 2)
        self.driver.setAcceleration(500,2)
        self.driver.setTargetSpeed(500, 3)
        self.driver.setAcceleration(500,3)
        self.driver.setTargetSpeed(500, 4)
        self.driver.setAcceleration(500,4)
        self.driver.setTargetSpeed(500, 5)
        self.driver.setAcceleration(500,5)

        #self.timer_list = nil
        # Shared memory
        self.array_timer_flag = Array('i', 6)   # 'i':integer * 6[array]
        self.process = Process(target=self.process_timer,args=[self.array_timer_flag,])
        self.process.start()

        self.logfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/StepMotor/LogFiles/'+self.prefix+'.log'
        self.intfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/StepMotor/LogFiles/int'+self.prefix+'.log'
        
        self.updatePVs()

    def __del__(self):
        self.process.kill()

    def read(self, channel):
        value = self.getParam(channel)
        return value

    def write(self, channel, value):
        print('%s => %s' % (channel, value))
        self.setParam(channel, value) # need !
        direction,name = channel.split("_")
        motorAddr = int(direction)
        if motorAddr < 0 or motorAddr > 5:
            print("Error motor Addr: %d",motorAddr)
#        if direction == "0":
#            motorAddr = 0
#        elif direction == "1":
#            motorAddr = 1
#        elif direction == "2":
#            motorAddr = 2
#        elif direction == "3":
#            motorAddr = 3
#        elif direction == "4":
#            motorAddr = 4
#        elif direction == "5":
#            motorAddr = 5
        #        with self.driver:
        if (name == "UPDATE") and (value == 1.0):
            self.driver.reconnect()
            
            pos = self.driver.getActualPosition(motorAddr)
            self.setParam(direction+"_POSITION",pos)

            d = datetime.now()
            with open(self.logfile,'a') as f:
                 f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+str(motorAddr)+' position updated as '+str(pos)+'\n')

        if name == "ACC":
            acc = self.getParam(direction+"_ACC")
            self.driver.setAcceleration(acc, motorAddr)
            
        if name == "VEL":
            vel = self.getParam(direction+"_VEL")
            self.driver.setTargetSpeed(vel, motorAddr)

        if name == "STOP":
            self.driver.stop(motorAddr)
## added 2019/08/06 ##
            pos =  self.driver.getActualPosition(motorAddr)
            self.setParam(direction+"_POSITION",pos)
####
            
        if name == "STEP":
            count = self.getParam(direction+"_STEP")
            pos =  self.driver.getActualPosition(motorAddr)
            self.driver.setTargetPosition(pos+count, motorAddr)

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+str(motorAddr)+' moved to '+str(pos+count)+'\n')
            
            #self.timer_list.append(channel)
            self.array_timer_flag[motorAddr] = 1

        self.updatePVs()
            
        return True

    def process_timer(self,array_timer_flag):
        while True:
            for motorAddr, state in enumerate(array_timer_flag):
                if state:
                    # Check stopped motor.
                    speed = self.driver.getActualSpeed(motorAddr)
                    if speed == 0:
                        # Stoped motor status.
                        array_timer_flag[motorAddr] = 0
                    # Check Limit switches.
                    direction = str(motorAddr)
                    value = self.driver.getRightLimitSwitch(motorAddr)
                    self.setParam(direction+"_RIGHTLIMITSWITCHSTATE",value)
                    print('%s => %d' % (direction+"_RIGHTLIMITSWITCHSTATE",value))
                    value = self.driver.getLeftLimitSwitch(motorAddr)
                    self.setParam(direction+"_LEFTLIMITSWITCHSTATE",value)
                    print('%s => %d' % (direction+"_LEFTLIMITSWITCHSTATE",value))
                    self.updatePVs()
                    
            time.sleep(1.0)

class PcasServer(pcaspy.SimpleServer):
    def __init__(self, prefix, driver):
        super(PcasServer, self).__init__()
        logging.info("initializing server...")
        self.server = pcaspy.SimpleServer()
        self.server.createPV(prefix, pvdb)
        driver = PcasDriver(driver,prefix)
        
    def run(self):
        logging.info("Starting server...")
        while True:
            self.server.process(0.1)
