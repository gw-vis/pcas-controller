# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:37:17 2018

@author: ayaka.shoda

Functions to actuate IP in each DOFs using stepping motors.
Tyere are three types of alignment of the stepping motors of IP in KAGRA, SR, BS, and TM.
The motor number assignment was defined in conf.py.
For more details, please refer KAGRA wiki (DGS/MotorControl/StepperMotor).
"""

import numpy as np
import conf
import userVariableMap

class IPMove:
    minA = 0
    maxA = 0
    minB = 0
    maxB = 0
    minC = 0
    maxC = 0

    def __init__(self, driver, part):
        #self.prefix = prefix
        self.part = part
        self.driver = driver

    def setLimitPosition(self, minA, maxA, minB, maxB, minC, maxC):
        self.minA = minA
        self.maxA = maxA
        self.minB = minB
        self.maxB = maxB
        self.minC = minC
        self.maxC = maxC

    ########## Actuation Functions ###########
    def Move_L(self,value):
        Type = conf.channel[self.part]["config"]
        motorA = conf.channel[self.part]["motorA"]
        motorB = conf.channel[self.part]["motorB"]
        motorC = conf.channel[self.part]["motorC"]
        signA = conf.channel[self.part]["signA"]
        signB = conf.channel[self.part]["signB"]
        signC = conf.channel[self.part]["signC"]
        
        posA = self.driver.getActualPosition(motorA)
        posB = self.driver.getActualPosition(motorB)
        posC = self.driver.getActualPosition(motorC)

        if Type == 'SR':
            #driver.setTargetPosition(posA+int(np.sqrt(3)/2*signA*value),motorA)
            #driver.setTargetPosition(posB-int(np.sqrt(3)/2*signB*value),motorB)
            countA =  int(np.sqrt(3)/2*signA*value)
            countB = -int(np.sqrt(3)/2*signB*value)
            countC = 0
#            countA =  int(2.0/np.sqrt(3)*signA*value)
#            countB = -int(2.0/np.sqrt(3)*signB*value)
#            countC = 0

        elif Type == 'BS':
            #driver.setTargetPosition(posA+int(np.sqrt(3)/2*signA*value),motorA)
            #driver.setTargetPosition(posB-int(np.sqrt(3)/2*signB*value),motorB)
            countA =  int(np.sqrt(3)/2*signA*value)
            countB = -int(np.sqrt(3)/2*signB*value)
            countC = 0
#            countA =  int(2.0/np.sqrt(3)*signA*value)
#            countB = 0
#            countC = -int(2.0/np.sqrt(3)*signB*value)

        elif Type == 'TM':
            #driver.setTargetPosition(posA+int(signA*value),motorA)
            #driver.setTargetPosition(posB-int(1/2*signB*value),motorB)
            #driver.setTargetPosition(posC-int(1/2*signC*value),motorC)
            countA =  int(signA*value)
            countB = -int(1.0/2.0*signB*value)
            countC = -int(1.0/2.0*signC*value)
#            countA =  int(signA*value)
#            countB = -int(2.0/1.0*signB*value)
#            countC = -int(2.0/1.0*signC*value)

        if countA != 0:
            countA = self.calcMoveRange(self.maxA,self.minA,posA,countA)
            self.driver.setTargetPosition(posA+countA,motorA)
            self.driver.setUserVariables(self.calcUserValiable(motorA,userVariable_actualPos),posA+countA)
            self.driver.storeUserVariables(self.calcUserValiable(motorA,userVariable_actualPos))

        if countB != 0:
            countB = self.calcMoveRange(self.maxB,self.minB,posB,countB)
            self.driver.setTargetPosition(posB+countB,motorB)
            self.driver.setUserVariables(self.calcUserValiable(motorB,userVariable_actualPos),posB+countB)
            self.driver.storeUserVariables(self.calcUserValiable(motorB,userVariable_actualPos))

        if countC != 0:
            countC = self.calcMoveRange(self.maxC,self.minC,posC,countC)
            self.driver.setTargetPosition(posC+countC,motorC)
            self.driver.setUserVariables(self.calcUserValiable(motorC,userVariable_actualPos),posC+countC)
            self.driver.storeUserVariables(self.calcUserValiable(motorC,userVariable_actualPos))

    def Move_T(self,value):
        Type = conf.channel[self.part]["config"]
        motorA = conf.channel[self.part]["motorA"]
        motorB = conf.channel[self.part]["motorB"]
        motorC = conf.channel[self.part]["motorC"]
        signA = conf.channel[self.part]["signA"]
        signB = conf.channel[self.part]["signB"]
        signC = conf.channel[self.part]["signC"]
        
        posA = self.driver.getActualPosition(motorA)
        posB = self.driver.getActualPosition(motorB)
        posC = self.driver.getActualPosition(motorC)
        
        if Type == 'SR':
            #driver.setTargetPosition(posC-int(signC*value),motorC)
            #driver.setTargetPosition(posB+int(1/2*signB*value),motorB)
            #driver.setTargetPosition(posA+int(1/2*signA*value),motorA)
            countC = -int(signC*value)
            countB =  int(1.0/2.0*signB*value)
            countA =  int(1.0/2.0*signA*value)
#            countC = -int(signC*value)
#            countB =  int(2.0/1.0*signB*value)
#            countA =  int(2.0/1.0*signA*value)

        elif Type == 'BS':
            #driver.setTargetPosition(posB+int(signB*value),motorB)
            #driver.setTargetPosition(posC-int(1/2*signC*value),motorC)
            #driver.setTargetPosition(posA-int(1/2*signA*value),motorA)
            countB =  int(signB*value)
            countC = -int(1.0/2.0*signC*value)
            countA = -int(1.0/2.0*signA*value)
#            countB =  int(signB*value)
#            countC = -int(2.0/1.0*signC*value)
#            countA = -int(2.0/1.0*signA*value)
            
        elif Type == 'TM':
            #driver.setTargetPosition(posB-int(np.sqrt(3)/2*signB*value),motorB)
            #driver.setTargetPosition(posC+int(np.sqrt(3)/2*signC*value),motorC)
            countB = -int(np.sqrt(3)/2.0*signB*value)
            countC =  int(np.sqrt(3)/2.0*signC*value)
            countA = 0
#            countB = -int(2.0/np.sqrt(3)*signB*value)
#            countC =  int(2.0/np.sqrt(3)*signC*value)
#            countA = 0

        if countA != 0:
            countA = self.calcMoveRange(self.maxA,self.minA,posA,countA)
            self.driver.setTargetPosition(posA+countA,motorA)
            self.driver.setUserVariables(self.calcUserValiable(motorA,userVariable_actualPos),posA+countA)
            self.driver.storeUserVariables(self.calcUserValiable(motorA,userVariable_actualPos))

        if countB != 0:
            countB = self.calcMoveRange(self.maxB,self.minB,posB,countB)
            self.driver.setTargetPosition(posB+countB,motorB)
            self.driver.setUserVariables(self.calcUserValiable(motorB,userVariable_actualPos),posB+countB)
            self.driver.storeUserVariables(self.calcUserValiable(motorB,userVariable_actualPos))

        if countC != 0:
            countC = self.calcMoveRange(self.maxC,self.minC,posC,countC)
            self.driver.setTargetPosition(posC+countC,motorC)
            self.driver.setUserVariables(self.calcUserValiable(motorC,userVariable_actualPos),posC+countC)
            self.driver.storeUserVariables(self.calcUserValiable(motorC,userVariable_actualPos))

    def Move_Y(self,value):
        motorA = conf.channel[self.part]["motorA"]
        motorB = conf.channel[self.part]["motorB"]
        motorC = conf.channel[self.part]["motorC"]
        signA = conf.channel[self.part]["signA"]
        signB = conf.channel[self.part]["signB"]
        signC = conf.channel[self.part]["signC"]
        
        posA = self.driver.getActualPosition(motorA)
        posB = self.driver.getActualPosition(motorB)
        posC = self.driver.getActualPosition(motorC)
        
        #driver.setTargetPosition(posA+int(signA*value),motorA)
        #driver.setTargetPosition(posB+int(signB*value),motorB)
        #driver.setTargetPosition(posC+int(signC*value),motorC)
        countA = int(signA*value)
        countB = int(signB*value)
        countC = int(signC*value)

        if countA != 0:
            countA = self.calcMoveRange(self.maxA,self.minA,posA,countA)
            self.driver.setTargetPosition(posA+countA,motorA)
            self.driver.setUserVariables(self.calcUserValiable(motorA,userVariable_actualPos),posA+countA)
            self.driver.storeUserVariables(self.calcUserValiable(motorA,userVariable_actualPos))

        if countB != 0:
            countB = self.calcMoveRange(self.maxB,self.minB,posB,countB)
            self.driver.setTargetPosition(posB+countB,motorB)
            self.driver.setUserVariables(self.calcUserValiable(motorB,userVariable_actualPos),posB+countB)
            self.driver.storeUserVariables(self.calcUserValiable(motorB,userVariable_actualPos))

        if countC != 0:
            countC = self.calcMoveRange(self.maxC,self.minC,posC,countC)
            self.driver.setTargetPosition(posC+countC,motorC)
            self.driver.setUserVariables(self.calcUserValiable(motorC,userVariable_actualPos),posC+countC)
            self.driver.storeUserVariables(self.calcUserValiable(motorC,userVariable_actualPos))


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
 
