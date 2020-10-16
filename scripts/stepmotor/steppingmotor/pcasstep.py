#!/usr/bin/env python

import os
import pcaspy
import conf
import logging
from datetime import datetime
import time

##################################################

pvdb ={
    '0_STEP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_ACC': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '0_VEL': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '0_STOP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '0_ERROR': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_STEP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_ACC': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '1_VEL': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '1_STOP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '1_ERROR': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_STEP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_ACC': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '2_VEL': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '2_STOP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '2_ERROR': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_STEP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_ACC': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '3_VEL': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '3_STOP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '3_ERROR': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_STEP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_ACC': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '4_VEL': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '4_STOP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '4_ERROR': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_STEP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_ACC': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '5_VEL': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 500,
    },
    '5_STOP': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_INTPOSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    '5_ERROR': {
        'desc': "move pico motor forward",
        'prec': 0,
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
        self.conf = conf
        self.prefix = prefix
        a, sus = prefix.split("-")
        self.part = sus[:-1]

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

        # setup limit and position from TMCM6100 mempry.
        for motorAddr in range(6):
            lrDistance = self.driver.getUserVariables(self.calcUserValiable(motorAddr,1))
            self.setParam(str(motorAddr)+"_LIMITPOSMAX",self.limitSwitchMax(lrDistance))
            self.setParam(str(motorAddr)+"_LIMITPOSMIN",self.limitSwitchMin(lrDistance))
            pos = self.driver.getUserVariables(self.calcUserValiable(motorAddr,2))
            self.setParam(str(motorAddr)+"_POSITION",pos)
            self.driver.stop(motorAddr)
            self.driver.setActualPosition(pos, motorAddr)
            if lrDistance == 0:
                self.driver.setRightLimitSwitchEnable(False, motorAddr)
                self.driver.setLeftLimitSwitchEnable(False,  motorAddr)
            else:
                self.driver.setRightLimitSwitchEnable(True, motorAddr)
                self.driver.setLeftLimitSwitchEnable(True,  motorAddr)

        self.logfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/StepMotor/LogFiles/'+self.prefix+'.log'
        self.intfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/StepMotor/LogFiles/int'+self.prefix+'.log'
        
        self.updatePVs()

    def read(self, channel):
        value = self.getParam(channel)
        print('%s => %s' % (channel, value))
        self.setParam(channel, value) # need !
        direction,name = channel.split("_")
        motorAddr = int(direction)
        if motorAddr < 0 or motorAddr > 5:
            print("Error motor Addr:",motorAddr)
        if name == "RSWITCH":
            value = self.driver.getRightLimitSwitch(motorAddr)
            self.setParam(direction+"_RSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))
        elif name == "LSWITCH":
            value = self.driver.getLeftLimitSwitch(motorAddr)
            self.setParam(direction+"_LSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))
        return value

    def write(self, channel, value):
        print('%s => %s' % (channel, value))
        self.setParam(channel, value) # need !
        direction,name = channel.split("_")
        motorAddr = int(direction)
        if motorAddr < 0 or motorAddr > 5:
            print("Error motor Addr:",motorAddr)
        #        with self.driver:
        if (name == "UPDATE") and (value == 1.0):
            #self.driver.reconnect()
            
            pos = self.driver.getActualPosition(motorAddr)
            if pos == 0:
                # Maybe after the power off. Read to EEPROM.
                pos = self.driver.getUserVariables(self.calcUserValiable(motorAddr,2))
            self.setParam(direction+"_POSITION",pos)

            d = datetime.now()
            with open(self.logfile,'a') as f:
                 f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+str(motorAddr)+' position updated as '+str(pos)+'\n')

            value = self.driver.getRightLimitSwitch(motorAddr)
            self.setParam(direction+"_RSWITCH",value)
            value = self.driver.getLeftLimitSwitch(motorAddr)
            self.setParam(direction+"_LSWITCH",value)

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
            self.driver.setUserVariables(self.calcUserValiable(motorAddr,2),pos)
            self.driver.storeUserVariables(self.calcUserValiable(motorAddr,2))

        if name == "STEP":
            count = self.getParam(direction+"_STEP")
            self.moveStepCount(motorAddr,direction,count)

        if name == "FWD":
            count = self.getParam(direction+"_FLUCTUATION")
            self.moveStepCount(motorAddr,direction,count)

        if name == "REV":
            count = -self.getParam(direction+"_FLUCTUATION")
            self.moveStepCount(motorAddr,direction,count)

        self.updatePVs()
            
        return True

    def moveStepCount(self,motorAddr,direction,count):
        pos =  self.driver.getActualPosition(motorAddr)
        axisDirection = self.conf.channel[self.part]["axisDirection"][motorAddr]
        min = self.getParam(direction+"_LIMITPOSMIN")
        max = self.getParam(direction+"_LIMITPOSMAX")
        count = self.calcMoveRange(max,min,pos,axisDirection*count)

        self.driver.setTargetPosition(pos+count, motorAddr)
        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+str(motorAddr)+' moved to '+str(pos+count)+'\n')            

        # Actual position.
        self.driver.setUserVariables(self.calcUserValiable(motorAddr,2),pos+count)
        self.driver.storeUserVariables(self.calcUserValiable(motorAddr,2))

    def calcUserValiable(self,motorAddr,offset):
        # CH.0 to 5
        number = motorAddr + offset * 6
        # EEPROM to #56.
        if number > 55:
            print "[Error] Over maximum number in EEPROM.", number
        return motorAddr + offset * 6

    def calcMoveRange(self,max,min,pos,count):
        if min == 0 and max == 0:
            #count = 0
            pass
        else:
            if count > 0 and max < pos + count:
                count = max - pos
            if count < 0 and min > pos + count:
                count = min - pos
        return count

    def limitSwitchMax(self,lrDistance):
        return int(lrDistance * 0.95)

    def limitSwitchMin(self,lrDistance):
        return int(lrDistance * 0.05)

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
