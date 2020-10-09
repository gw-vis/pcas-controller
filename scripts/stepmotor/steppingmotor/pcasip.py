#!/usr/bin/env python

import os
import pcaspy
import conf
import logging
import funcIP
from datetime import datetime
import time

##################################################
pvdb ={
    'L_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'T_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'Y_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'F0Y_STEP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'ACC': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    'VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 500,
    },
    'STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'A_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_POSITION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_RSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_LSWITCH': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_LIMITPOSMAX': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_LIMITPOSMIN': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_INIT': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'UPDATE': {
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

        self.logfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/StepMotor/LogFiles/'+self.prefix+'.log'

        self.updatePVs()
        self.ipmove = funcIP.IPMove(driver,self.part)

        # setup limit and position from TMCM6100 mempry.
        motorAddrA  = self.conf.channel[self.part]["motorA"]
        motorAddrB  = self.conf.channel[self.part]["motorB"]
        motorAddrC  = self.conf.channel[self.part]["motorC"]
        motorAddrY  = self.conf.channel[self.part]["motorY"]

        self.motorInitilize(motorAddrA,"A")
        self.motorInitilize(motorAddrB,"B")
        self.motorInitilize(motorAddrC,"C")
        self.motorInitilize(motorAddrY,"F0Y")

    def motorInitilize(self,motorAddr,dof):
        lrDistance = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,1))
        self.setParam(dof+"_LIMITPOSMAX",self.limitSwitchMax(lrDistance))
        self.setParam(dof+"_LIMITPOSMIN",self.limitSwitchMin(lrDistance))
        pos = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,2))
        self.setParam(dof+"_POSITION",pos)
        self.driver.stop(motorAddr)
        self.driver.setActualPosition(pos, motorAddr)
        if lrDistance == 0:
            self.driver.setRightLimitSwitchEnable(False, motorAddr)
            self.driver.setLeftLimitSwitchEnable(False,  motorAddr)
        else:
            self.driver.setRightLimitSwitchEnable(True, motorAddr)
            self.driver.setLeftLimitSwitchEnable(True,  motorAddr)

    def read(self, channel):
        value = self.getParam(channel)
        logging.info('%s == %s' % (channel, value))

        motorAddrA  = self.conf.channel[self.part]["motorA"]
        motorAddrB  = self.conf.channel[self.part]["motorB"]
        motorAddrC  = self.conf.channel[self.part]["motorC"]
        motorAddrY  = self.conf.channel[self.part]["motorY"]
        
        if channel == "A_RSWITCH":
            value = self.driver.getRightLimitSwitch(motorAddrA)
            self.setParam("A_RSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif channel == "B_RSWITCH":
            value = self.driver.getRightLimitSwitch(motorAddrB)
            self.setParam("B_RSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif channel == "C_RSWITCH":
            value = self.driver.getRightLimitSwitch(motorAddrC)
            self.setParam("C_RSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif channel == "F0Y_RSWITCH":
            value = self.driver.getRightLimitSwitch(motorAddrY)
            self.setParam("F0Y_RSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif channel == "A_LSWITCH":
            value = self.driver.getLeftLimitSwitch(motorAddrA)
            self.setParam("A_LSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif channel == "B_LSWITCH":
            value = self.driver.getLeftLimitSwitch(motorAddrB)
            self.setParam("B_LSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif channel == "C_LSWITCH":
            value = self.driver.getLeftLimitSwitch(motorAddrC)
            self.setParam("C_LSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif channel == "F0Y_LSWITCH":
            value = self.driver.getLeftLimitSwitch(motorAddrY)
            self.setParam("F0Y_LSWITCH",value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        return value

    def write(self, channel, value):
        print('%s => %s' % (channel, value))
        self.setParam(channel, value)
        #driverAddr = self.conf.channel[self.prefix+channel[:3]]["driver"]
        motorAddrA  = self.conf.channel[self.part]["motorA"]
        motorAddrB  = self.conf.channel[self.part]["motorB"]
        motorAddrC  = self.conf.channel[self.part]["motorC"]
        motorAddrY  = self.conf.channel[self.part]["motorY"]
        
        #        with self.driver:
        if (channel == "UPDATE") and (value == 1.0):
    #        self.driver.reconnect()
            
            posA = self.driver.getActualPosition(motorAddrA)
            if posA == 0:
                # Maybe after the power off. Read to EEPROM.
                posA = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrA,2))
            self.setParam("A_POSITION",posA)
            posB = self.driver.getActualPosition(motorAddrB)
            if posB == 0:
                # Maybe after the power off. Read to EEPROM.
                posB = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrB,2))
            self.setParam("B_POSITION",posB)
            posC = self.driver.getActualPosition(motorAddrC)
            if posC == 0:
                # Maybe after the power off. Read to EEPROM.
                posC = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrC,2))
            self.setParam("C_POSITION",posC)
            posY = self.driver.getActualPosition(motorAddrY)
            if posY == 0:
                # Maybe after the power off. Read to EEPROM.
                posY = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrY,2))
            self.setParam("F0Y_POSITION",posY)
        
            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' position updated as motorA:'+str(posA)+' motorB:'+str(posB)+' motorC:'+str(posC)+' F0Y:'+str(posY)+'\n')

            value = self.driver.getRightLimitSwitch(motorAddrA)
            self.setParam("A_RSWITCH",value)
            value = self.driver.getRightLimitSwitch(motorAddrB)
            self.setParam("B_RSWITCH",value)
            value = self.driver.getRightLimitSwitch(motorAddrC)
            self.setParam("C_RSWITCH",value)
            value = self.driver.getRightLimitSwitch(motorAddrY)
            self.setParam("F0Y_RSWITCH",value)
            value = self.driver.getLeftLimitSwitch(motorAddrA)
            self.setParam("A_LSWITCH",value)
            value = self.driver.getLeftLimitSwitch(motorAddrB)
            self.setParam("B_LSWITCH",value)
            value = self.driver.getLeftLimitSwitch(motorAddrC)
            self.setParam("C_LSWITCH",value)
            value = self.driver.getLeftLimitSwitch(motorAddrY)
            self.setParam("F0Y_LSWITCH",value)

        if channel == "ACC":
            acc = self.getParam("ACC")
            self.driver.setAcceleration(acc, motorAddrA)
            self.driver.setAcceleration(acc, motorAddrB)
            self.driver.setAcceleration(acc, motorAddrC)
            self.driver.setAcceleration(acc, motorAddrY)
            
        if channel == "VEL":
            vel = self.getParam("VEL")
            self.driver.setTargetSpeed(vel, motorAddrA)
            self.driver.setTargetSpeed(vel, motorAddrB)
            self.driver.setTargetSpeed(vel, motorAddrC)
            self.driver.setTargetSpeed(vel, motorAddrY)
            
        if channel == "STOP":
            self.driver.stop(motorAddrA)
            self.driver.stop(motorAddrB)
            self.driver.stop(motorAddrC)
            self.driver.stop(motorAddrY)

            pos =  self.driver.getActualPosition(motorAddrA)
            self.setParam("A_POSITION",pos)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrA,2),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrA,2))

            pos =  self.driver.getActualPosition(motorAddrB)
            self.setParam("B_POSITION",pos)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrB,2),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrB,2))

            pos =  self.driver.getActualPosition(motorAddrC)
            self.setParam("C_POSITION",pos)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrC,2),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrC,2))

            pos =  self.driver.getActualPosition(motorAddrY)
            self.setParam("F0Y_POSITION",pos)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrY,2),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrY,2))

        if channel == "L_STEP":
            self.ipmove.setLimitPosition(
                self.getParam("A_LIMITPOSMIN"),
                self.getParam("A_LIMITPOSMAX"),
                self.getParam("B_LIMITPOSMIN"),
                self.getParam("B_LIMITPOSMAX"),
                self.getParam("C_LIMITPOSMIN"),
                self.getParam("C_LIMITPOSMAX"))

            self.ipmove.Move_L(value)
            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' IP moved in L by '+str(value)+'\n')

        if channel == "T_STEP":
            self.ipmove.setLimitPosition(
                self.getParam("A_LIMITPOSMIN"),
                self.getParam("A_LIMITPOSMAX"),
                self.getParam("B_LIMITPOSMIN"),
                self.getParam("B_LIMITPOSMAX"),
                self.getParam("C_LIMITPOSMIN"),
                self.getParam("C_LIMITPOSMAX"))

            self.ipmove.Move_T(value)
            
            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' IP moved in T by '+str(value)+'\n')

        if channel == "Y_STEP":
            self.ipmove.setLimitPosition(
                self.getParam("A_LIMITPOSMIN"),
                self.getParam("A_LIMITPOSMAX"),
                self.getParam("B_LIMITPOSMIN"),
                self.getParam("B_LIMITPOSMAX"),
                self.getParam("C_LIMITPOSMIN"),
                self.getParam("C_LIMITPOSMAX"))

            self.ipmove.Move_Y(value)
            
            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' IP moved in Y by '+str(value)+'\n')

        if channel == "F0Y_STEP":
            signY = self.conf.channel[self.part]["signY"]
            pos = self.driver.getActualPosition(motorAddrY)

            min = self.getParam("F0Y_LIMITPOSMIN")
            max = self.getParam("F0Y_LIMITPOSMAX")
            count = self.ipmove.calcMoveRange(max,min,pos,signY*value)

            self.driver.setTargetPosition(pos+count, motorAddrY)
            
            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' F0Y moved by '+str(value)+'\n')

        self.updatePVs()
        
        return True

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
