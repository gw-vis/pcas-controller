#!/usr/bin/env python

import os
import pcaspy
import conf
import logging
import funcIP
from datetime import datetime
import time
import userVariableMap

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
        'value': 10,
    },
    'VEL': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 10,
    },
    'STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'A_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'B_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'C_STOP': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'F0Y_STOP': {
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
    'A_LIMITCHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_LIMITCHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_LIMITCHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_LIMITCHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'L_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'T_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'Y_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'L_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'T_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'Y_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'L_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'T_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'Y_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_LRDISTANCE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_LRDISTANCE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_LRDISTANCE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_LRDISTANCE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_LRDISTANCECHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_LRDISTANCECHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_LRDISTANCECHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_LRDISTANCECHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'A_POSITIONCHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'B_POSITIONCHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'C_POSITIONCHANGE': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'F0Y_POSITIONCHANGE': {
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
    },
    'A_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'B_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'C_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    },
    'F0Y_UPDATE': {
        'desc': "move pico motor forward",
        'prec': 4,
        'value': 0,
    }
}

motor_dict = {
    'A':   'motorA',
    'B':   'motorB',
    'C':   'motorC',
    'F0Y': 'motorY'
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
        
        self.driver.setTargetSpeed(10, 0)
        self.driver.setAcceleration(10,0)
        self.driver.setTargetSpeed(10, 1)
        self.driver.setAcceleration(10,1)
        self.driver.setTargetSpeed(10, 2)
        self.driver.setAcceleration(10,2)
        self.driver.setTargetSpeed(10, 3)
        self.driver.setAcceleration(10,3)
        self.driver.setTargetSpeed(10, 4)
        self.driver.setAcceleration(10,4)
        self.driver.setTargetSpeed(10, 5)
        self.driver.setAcceleration(10,5)

        self.logfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/StepMotor/LogFiles/'+self.prefix+'.log'

        self.updatePVs()
        self.ipmove = funcIP.IPMove(driver,self.part,self.logfile)

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
        limitMax = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax))
        self.setParam(dof+"_LIMITPOSMAX",limitMax)
        limitMin = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin))
        self.setParam(dof+"_LIMITPOSMIN",limitMin)
        pos = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.actualPos))
        self.setParam(dof+"_POSITION",pos)
        self.driver.stop(motorAddr)
        self.driver.setActualPosition(pos, motorAddr)
        lrDistance = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.lrDistance))
        self.setParam(dof+"_LRDISTANCE",lrDistance)
        if lrDistance == 0:
            self.driver.setRightLimitSwitchEnable(False, motorAddr)
            self.driver.setLeftLimitSwitchEnable(False,  motorAddr)
        else:
            self.driver.setRightLimitSwitchEnable(True, motorAddr)
            self.driver.setLeftLimitSwitchEnable(True,  motorAddr)

        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+str(motorAddr)+' initialize actual position '+str(pos)+' limit '+str(limitMax)+' , '+str(limitMin)+' Distance '+str(lrDistance)+'\n')

    def read(self, channel):
        value = self.getParam(channel)
        logging.info('%s == %s' % (channel, value))

        if '_' in channel:
            direction,name = channel.split("_")
        else:
            direction = ""
            name = channel

        if name == "RSWITCH":
            motorAddr  = self.conf.channel[self.part][motor_dict[direction]]
            value = self.driver.getRightLimitSwitch(motorAddr)
            self.setParam(channel,value)
            self.updatePVs()
            print('%s => %d' % (channel, value))

        elif name == "LSWITCH":
            motorAddr  = self.conf.channel[self.part][motor_dict[direction]]
            value = self.driver.getLeftLimitSwitch(motorAddr)
            self.setParam(channel,value)
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
        
        if '_' in channel:
            direction,name = channel.split("_")
        else:
            direction = ""
            name = channel

        #        with self.driver:
        if (name == "UPDATE") and (value == 1.0):
    #        self.driver.reconnect()
            
            posA = self.driver.getActualPosition(motorAddrA)
            if posA == 0:
                # Maybe after the power off. Read to EEPROM.
                posA = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrA,userVariableMap.actualPos))
            self.setParam("A_POSITION",posA)
            posB = self.driver.getActualPosition(motorAddrB)
            if posB == 0:
                # Maybe after the power off. Read to EEPROM.
                posB = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrB,userVariableMap.actualPos))
            self.setParam("B_POSITION",posB)
            posC = self.driver.getActualPosition(motorAddrC)
            if posC == 0:
                # Maybe after the power off. Read to EEPROM.
                posC = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrC,userVariableMap.actualPos))
            self.setParam("C_POSITION",posC)
            posY = self.driver.getActualPosition(motorAddrY)
            if posY == 0:
                # Maybe after the power off. Read to EEPROM.
                posY = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddrY,userVariableMap.actualPos))
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

        if name == "ACC":
            acc = self.getParam("ACC")
            self.driver.setAcceleration(acc, motorAddrA)
            self.driver.setAcceleration(acc, motorAddrB)
            self.driver.setAcceleration(acc, motorAddrC)
            self.driver.setAcceleration(acc, motorAddrY)

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' acc as motor:'+str(acc)+'\n')

        if name == "VEL":
            vel = self.getParam("VEL")
            self.driver.setTargetSpeed(vel, motorAddrA)
            self.driver.setTargetSpeed(vel, motorAddrB)
            self.driver.setTargetSpeed(vel, motorAddrC)
            self.driver.setTargetSpeed(vel, motorAddrY)

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' vel as motor:'+str(vel)+'\n')

        if (name == "STOP") and (value == 1.0):
            self.driver.stop(motorAddrA)
            self.driver.stop(motorAddrB)
            self.driver.stop(motorAddrC)
            self.driver.stop(motorAddrY)

            posA =  self.driver.getActualPosition(motorAddrA)
            self.setParam("A_POSITION",posA)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrA,userVariableMap.actualPos),posA)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrA,userVariableMap.actualPos))

            posB =  self.driver.getActualPosition(motorAddrB)
            self.setParam("B_POSITION",posB)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrB,userVariableMap.actualPos),posB)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrB,userVariableMap.actualPos))

            posC =  self.driver.getActualPosition(motorAddrC)
            self.setParam("C_POSITION",posC)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrC,userVariableMap.actualPos),posC)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrC,userVariableMap.actualPos))

            posY =  self.driver.getActualPosition(motorAddrY)
            self.setParam("F0Y_POSITION",posY)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrY,userVariableMap.actualPos),posY)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrY,userVariableMap.actualPos))

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' position stoped as motorA:'+str(posA)+' motorB:'+str(posB)+' motorC:'+str(posC)+' F0Y:'+str(posY)+'\n')

        if name == "STEP":
            self.moveStepCount(value,direction)

        if (name == "FWD") and (value == 1.0):
            count = self.getParam(direction+"_FLUCTUATION")
            self.moveStepCount(count,direction)

        if (name == "REV") and (value == 1.0):
            count = -self.getParam(direction+"_FLUCTUATION")
            self.moveStepCount(count,direction)

        if (name == "LIMITCHANGE") and (value == 1.0):
            self.LimitChange(direction)

        if (name == "LRDISTANCECHANGE") and (value == 1.0):
            self.lrDistanceChange(direction)

        if (name == "POSITIONCHANGE") and (value == 1.0):
            self.PositionChange(direction)

        self.updatePVs()
        
        return True

    def moveStepCount(self,count,direction):
        self.ipmove.setLimitPosition(
            self.getParam("A_LIMITPOSMIN"),
            self.getParam("A_LIMITPOSMAX"),
            self.getParam("B_LIMITPOSMIN"),
            self.getParam("B_LIMITPOSMAX"),
            self.getParam("C_LIMITPOSMIN"),
            self.getParam("C_LIMITPOSMAX"))

        if direction == 'L':
            axisDirection = self.conf.channel[self.part]["axisDirectionLEN"]
            self.ipmove.Move_L(axisDirection*count)
        elif direction == 'T':
            axisDirection = self.conf.channel[self.part]["axisDirectionTRA"]
            self.ipmove.Move_T(axisDirection*count)
        elif direction == 'Y':
            axisDirection = self.conf.channel[self.part]["axisDirectionYAW"]
            self.ipmove.Move_Y(axisDirection*count)

        elif direction in ['A','B','C','F0Y']:
            motorAddr  = self.conf.channel[self.part][motor_dict[direction]]

            axisDirection = self.conf.channel[self.part]["axisDirection"+direction]  # Direction to sensor.
            pos = self.driver.getActualPosition(motorAddr)

            min = self.getParam(direction+"_LIMITPOSMIN")
            max = self.getParam(direction+"_LIMITPOSMAX")
            count = self.ipmove.calcMoveRange(max,min,pos,axisDirection*count)

            self.driver.setTargetPosition(pos+count, motorAddr)

            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.actualPos),pos+count)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.actualPos))

            d = datetime.now()
            with open(self.logfile,'a') as f:
                f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' IP moved in '+direction+' to '+str(pos+count)+' from '+str(pos)+'\n')

    def LimitChange(self,direction):
        motorAddr  = self.conf.channel[self.part][motor_dict[direction]]
        limitMin = self.getParam(direction+"_LIMITPOSMIN")
        limitMax = self.getParam(direction+"_LIMITPOSMAX")
        oldlimitMax = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax))
        oldlimitMin = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin))

        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+direction+' limit change to '+str(limitMin)+' , '+str(limitMax)+' from '+str(oldlimitMin)+' , '+str(oldlimitMax)+'\n')            

        # limitMin and limitMax position.
        self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin),limitMin)
        self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax),limitMax)
        # Store all paranator to EEPROM.
        print("[Start]Store TMCM6110 EEPROM ",direction)
        self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin))
        self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax))
        print("[End]Store TMCM6110 EEPROM")

    def lrDistanceChange(self,direction):
        motorAddr  = self.conf.channel[self.part][motor_dict[direction]]
        lrDistance = self.getParam(direction+"_LRDISTANCE")
        if lrDistance == 0:
            self.driver.setRightLimitSwitchEnable(False, motorAddr)
            self.driver.setLeftLimitSwitchEnable(False,  motorAddr)
        else:
            self.driver.setRightLimitSwitchEnable(True, motorAddr)
            self.driver.setLeftLimitSwitchEnable(True,  motorAddr)
        oldlrDistance = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.lrDistance))

        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+direction+' lrdistance change to '+str(lrDistance)+' from '+str(oldlrDistance)+'\n')            

        # limitMin and limitMax position.
        self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.lrDistance),lrDistance)
        # Store all paranator to EEPROM.
        print("[Start]Store TMCM6110 EEPROM")
        self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.lrDistance))
        print("[End]Store TMCM6110 EEPROM")

    def PositionChange(self,direction):
        motorAddr  = self.conf.channel[self.part][motor_dict[direction]]
        pos = self.getParam(direction+"_POSITION")
        self.driver.stop(motorAddr)
        self.driver.setActualPosition(pos, motorAddr)
        oldpos = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.actualPos))

        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+direction+' Position change to '+str(pos)+' from '+str(oldpos)+'\n')            

        # limitMin and limitMax position.
        self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.actualPos),pos)
        # Store all paranator to EEPROM.
        print("[Start]Store TMCM6110 EEPROM")
        self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.actualPos))
        print("[End]Store TMCM6110 EEPROM")

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
