#!/usr/bin/env python3

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
    'H1_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'H2_FLUCTUATION': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'H3_FLUCTUATION': {
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
    'H1_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'H2_FWD': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'H3_FWD': {
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
    'H1_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'H2_REV': {
        'desc': "move pico motor forward",
        'prec': 0,
        'value': 0,
    },
    'H3_REV': {
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
        limitMax = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax))
        self.setParam(dof+"_LIMITPOSMAX",limitMax)
        limitMin = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin))
        self.setParam(dof+"_LIMITPOSMIN",limitMin)
        pos = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.actualPos))
        self.setParam(dof+"_POSITION",pos)
        self.driver.stop(motorAddr)
        self.driver.setActualPosition(pos, motorAddr)
        lrDistance = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.lrDistance))
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
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrA,userVariableMap.actualPos),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrA,userVariableMap.actualPos))

            pos =  self.driver.getActualPosition(motorAddrB)
            self.setParam("B_POSITION",pos)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrB,userVariableMap.actualPos),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrB,userVariableMap.actualPos))

            pos =  self.driver.getActualPosition(motorAddrC)
            self.setParam("C_POSITION",pos)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrC,userVariableMap.actualPos),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrC,userVariableMap.actualPos))

            pos =  self.driver.getActualPosition(motorAddrY)
            self.setParam("F0Y_POSITION",pos)
            self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddrY,userVariableMap.actualPos),pos)
            self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddrY,userVariableMap.actualPos))

        if channel == "L_STEP":
            self.moveStepCount(value,'L')

        if channel == "T_STEP":
            self.moveStepCount(value,'T')

        if channel == "Y_STEP":
            self.moveStepCount(value,'Y')

        if channel == "F0Y_STEP":
           self.moveStepCount(value,'F0Y')

        if (channel == "L_FWD") and (value == 1.0):
            count = self.getParam("L_FLUCTUATION")
            self.moveStepCount(count,'L')

        if (channel == "L_REV") and (value == 1.0):
            count = -self.getParam("L_FLUCTUATION")
            self.moveStepCount(count,'L')

        if (channel == "T_FWD") and (value == 1.0):
            count = self.getParam("T_FLUCTUATION")
            self.moveStepCount(count,'T')

        if (channel == "T_REV") and (value == 1.0):
            count = -self.getParam("T_FLUCTUATION")
            self.moveStepCount(count,'T')

        if (channel == "Y_FWD") and (value == 1.0):
            count = self.getParam("Y_FLUCTUATION")
            self.moveStepCount(count,'Y')

        if (channel == "Y_REV") and (value == 1.0):
            count = -self.getParam("Y_FLUCTUATION")
            self.moveStepCount(count,'Y')

        if (channel == "F0Y_FWD") and (value == 1.0):
            count = self.getParam("F0Y_FLUCTUATION")
            self.moveStepCount(count,'F0Y')

        if (channel == "F0Y_REV") and (value == 1.0):
            count = -self.getParam("F0Y_FLUCTUATION")
            self.moveStepCount(count,'F0Y')

        if (channel == "H1_FWD") and (value == 1.0):
            count = self.getParam("H1_FLUCTUATION")
            self.moveStepCount(count,'H1')

        if (channel == "H1_REV") and (value == 1.0):
            count = -self.getParam("H1_FLUCTUATION")
            self.moveStepCount(count,'H1')

        if (channel == "H2_FWD") and (value == 1.0):
            count = self.getParam("H2_FLUCTUATION")
            self.moveStepCount(count,'H2')

        if (channel == "H2_REV") and (value == 1.0):
            count = -self.getParam("H2_FLUCTUATION")
            self.moveStepCount(count,'H2')

        if (channel == "H3_FWD") and (value == 1.0):
            count = self.getParam("H3_FLUCTUATION")
            self.moveStepCount(count,'H3')

        if (channel == "H3_REV") and (value == 1.0):
            count = -self.getParam("H3_FLUCTUATION")
            self.moveStepCount(count,'H3')

        if (channel == "A_LIMITCHANGE") and (value == 1.0):
            self.LimitChange(motorAddrA,'A')

        if (channel == "B_LIMITCHANGE") and (value == 1.0):
            self.LimitChange(motorAddrB,'B')

        if (channel == "C_LIMITCHANGE") and (value == 1.0):
            self.LimitChange(motorAddrC,'C')

        if (channel == "F0Y_LIMITCHANGE") and (value == 1.0):
            self.LimitChange(motorAddrY,'F0Y')

        self.updatePVs()
        
        return True

    def moveStepCount(self,count,dirStr):
        self.ipmove.setLimitPosition(
            self.getParam("A_LIMITPOSMIN"),
            self.getParam("A_LIMITPOSMAX"),
            self.getParam("B_LIMITPOSMIN"),
            self.getParam("B_LIMITPOSMAX"),
            self.getParam("C_LIMITPOSMIN"),
            self.getParam("C_LIMITPOSMAX"))

        if dirStr == 'L':
            axisDirection = self.conf.channel[self.part]["axisDirectionLEN"]
            self.ipmove.Move_L(axisDirection*count)
        elif dirStr == 'T':
            axisDirection = self.conf.channel[self.part]["axisDirectionTRA"]
            self.ipmove.Move_T(axisDirection*count)
        elif dirStr == 'Y':
            axisDirection = self.conf.channel[self.part]["axisDirectionYAW"]
            self.ipmove.Move_Y(axisDirection*count)
        elif dirStr == 'F0Y':
            motorAddrY  = self.conf.channel[self.part]["motorY"]
       
            signY = self.conf.channel[self.part]["signY"]
            axisDirection = self.conf.channel[self.part]["axisDirectionF0Y"]
            pos = self.driver.getActualPosition(motorAddrY)

            min = self.getParam("F0Y_LIMITPOSMIN")
            max = self.getParam("F0Y_LIMITPOSMAX")
            count = self.ipmove.calcMoveRange(max,min,pos,signY*axisDirection*count)

            self.driver.setTargetPosition(pos+count, motorAddrY)

        elif dirStr == 'H1':
            motorAddrA  = self.conf.channel[self.part]["motorA"]
       
            axisDirection = self.conf.channel[self.part]["axisDirectionA"]  # Direction to sensor.
            pos = self.driver.getActualPosition(motorAddrA)

            min = self.getParam("A_LIMITPOSMIN")
            max = self.getParam("A_LIMITPOSMAX")
            count = self.ipmove.calcMoveRange(max,min,pos,axisDirection*count)

            self.driver.setTargetPosition(pos+count, motorAddrA)

        elif dirStr == 'H2':
            motorAddrB  = self.conf.channel[self.part]["motorB"]
       
            axisDirection = self.conf.channel[self.part]["axisDirectionB"]  # Direction to sensor.
            pos = self.driver.getActualPosition(motorAddrB)

            min = self.getParam("B_LIMITPOSMIN")
            max = self.getParam("B_LIMITPOSMAX")
            count = self.ipmove.calcMoveRange(max,min,pos,axisDirection*count)

            self.driver.setTargetPosition(pos+count, motorAddrB)

        elif dirStr == 'H3':
            motorAddrC  = self.conf.channel[self.part]["motorC"]
       
            axisDirection = self.conf.channel[self.part]["axisDirectionC"]  # Direction to sensor.
            pos = self.driver.getActualPosition(motorAddrC)

            min = self.getParam("C_LIMITPOSMIN")
            max = self.getParam("C_LIMITPOSMAX")
            count = self.ipmove.calcMoveRange(max,min,pos,axisDirection*count)

            self.driver.setTargetPosition(pos+count, motorAddrC)

        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' IP moved in '+dirStr+' by '+str(count)+'\n')

    def LimitChange(self,motorAddr,dirStr):
        limitMin = self.getParam(dirStr+"_LIMITPOSMIN")
        limitMax = self.getParam(dirStr+"_LIMITPOSMAX")
        oldlimitMax = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax))
        oldlimitMin = self.driver.getUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin))

        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+str(motorAddr)+':'+dirStr+' limit change to '+str(limitMin)+' , '+str(limitMax)+' from '+str(oldlimitMin)+' , '+str(oldlimitMax)+'\n')            

        # limitMin and limitMax position.
        self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin),limitMin)
        self.driver.setUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax),limitMax)
        # Store all paranator to EEPROM.
        print("[Start]Store TMCM6110 EEPROM ",dirStr)
        self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMin))
        self.driver.storeUserVariables(self.ipmove.calcUserValiable(motorAddr,userVariableMap.limitMax))
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
