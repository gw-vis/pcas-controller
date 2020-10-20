#!/usr/bin/env python3
import os
import sys
from Trinamic_control6110 import *
from datetime import datetime
import time
import conf
#from epics import caget, caput, cainfo
import userVariableMap

driverDict = {
    "PR2_GAS"   :"10.68.150.40",
    "PR0_GAS"   :"10.68.150.41",
    "ITMX_GAS"  :"10.68.150.43",
    "ITMX_IP"   :"10.68.150.44",
    "ETMX_GAS"  :"10.68.150.45",
    "ETMX_IP"   :"10.68.150.46",
    "ITMY_GAS"  :"10.68.150.47",
    "ITMY_IP"   :"10.68.150.48",
    "ETMY_GAS"  :"10.68.150.49",
    "ETMY_IP"   :"10.68.150.50",
    "BS_GAS"    :"10.68.150.51",
    "BS_IP"     :"10.68.150.52",
    "SR2_GAS"   :"10.68.150.53",
    "SR2_IP"    :"10.68.150.54",
    "SR3_GAS"   :"10.68.150.55",
    "SR3_IP"    :"10.68.150.56",
    "SRM_GAS"   :"10.68.150.57",
    "SRM_IP"    :"10.68.150.58",
    # for Testing.
    "TEST_GAS"  :"10.68.150.63",
    "TESTSR_IP" :"10.68.150.63"
}

def getlogfileName(prefix):
    return '/kagra/Dropbox/Subsystems/VIS/Scripts/StepMotor/LogFiles/'+prefix+'.log'

def wait_moving_motor(driver,sleeptime,motorAddr):
    isError = False
    count = sleeptime
    while True:
        time.sleep(1)
        actualSpeed = driver.getActualSpeed(motorAddr)
        if actualSpeed == 0:
            break
        if count == 0:
            print('Error: Time Out')
            isError = True
            break
        count = count - 1
    return isError

def calcUserValiable(motorAddr,offset):
    # CH.0 to 5
    number = motorAddr + offset * 6
    # EEPROM to #56.
    if number > 55:
        print("[Error] Over maximum number in EEPROM.", number)
    return motorAddr + offset * 6

def calcMoveRange(max,min,pos,count):
    if min == 0 and max == 0:
        count = 0
    else:
        if count > 0 and max < pos + count:
            count = max - pos
        if count < 0 and min > pos + count:
            count = min - pos
    return count

def limitSwitchMax(lrDistance):
    return int(lrDistance * 0.95)

def limitSwitchMin(lrDistance):
    return int(lrDistance * 0.05)

def initialize(driver,motorAddr,prefix):
    rswitch = driver.getRightLimitSwitch(motorAddr)
    lswitch = driver.getLeftLimitSwitch(motorAddr)
    if rswitch == 1 and lswitch == 1:
        print('Both Limit switch ON')
        return

    driver.setRightLimitSwitchEnable(True, motorAddr)
    driver.setLeftLimitSwitchEnable(True,  motorAddr)
    # First step is search distance to Home Position from Left(Zero) position.
    count = driver.getMinRange()  # set maximum value
    driver.stop(motorAddr)
    driver.setActualPosition(0, motorAddr)
    pos = driver.getActualPosition(motorAddr)
    driver.setTargetPosition(pos+count, motorAddr)
    # to left.
    isError = wait_moving_motor(driver,120, motorAddr)
    rswitch = driver.getRightLimitSwitch(motorAddr)
    lswitch = driver.getLeftLimitSwitch(motorAddr)
    if rswitch == 0 and lswitch == 1:
        # Zero is Left position.
        homePos = -driver.getActualPosition(motorAddr)
    else:
        homePos = 0
        print('Not found Left Limit switch')
        return

    # Second step is search distance to Right Position from Left(Zero) position.
    # to Right
    count = driver.getMaxRange() # set maximum value
    driver.setActualPosition(0, motorAddr)
    pos = driver.getActualPosition(motorAddr)
    driver.setTargetPosition(pos+count, motorAddr)
    # to left.
    isError = wait_moving_motor(driver,120, motorAddr)
    rswitch = driver.getRightLimitSwitch(motorAddr)
    lswitch = driver.getLeftLimitSwitch(motorAddr)
    if rswitch == 1 and lswitch == 0:
        # Left to Right distance.
        lrDistance = driver.getActualPosition(motorAddr)
    else:
        lrDistance = 0
        print('Not found Right Limit switch')
        return

#    caput(prefix+"_LIMITPOSMAX",limitSwitchMax(lrDistance))
#    caput(prefix+"_LIMITPOSMIN",limitSwitchMin(lrDistance))

    # Move to Homep osition.
    driver.setTargetPosition(homePos, motorAddr)
#    caput(prefix+"_POSITION",homePos)
    print(prefix, lrDistance, homePos)

    limitMin = limitSwitchMin(lrDistance)
    limitMax = limitSwitchMax(lrDistance)
    print(limitMin,limitMax)

    ## Write to EEPROM(TMCM6110).
    # Write all RAM memory.
    # Home Position.
    driver.setUserVariables(calcUserValiable(motorAddr,userVariableMap.homePos),homePos)
    # L-R Distance.
    driver.setUserVariables(calcUserValiable(motorAddr,userVariableMap.lrDistance),lrDistance)
    # Actual position.
    driver.setUserVariables(calcUserValiable(motorAddr,userVariableMap.actualPos),homePos)
    # limitMin position.
    driver.setUserVariables(calcUserValiable(motorAddr,userVariableMap.limitMin),limitMin)
    # limitMax position.
    driver.setUserVariables(calcUserValiable(motorAddr,userVariableMap.limitMax),limitMax)
    # Store all paranator to EEPROM.
    print("[Start]Store TMCM6110 EEPROM")
    driver.storeUserVariables(calcUserValiable(motorAddr,userVariableMap.homePos))
    driver.storeUserVariables(calcUserValiable(motorAddr,userVariableMap.lrDistance))
    driver.storeUserVariables(calcUserValiable(motorAddr,userVariableMap.actualPos))
    driver.storeUserVariables(calcUserValiable(motorAddr,userVariableMap.limitMin))
    driver.storeUserVariables(calcUserValiable(motorAddr,userVariableMap.limitMax))
    print("[End]Store TMCM6110 EEPROM")

    d = datetime.now()
    with open(getlogfileName(prefix),'a') as f:
        f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' motor'+str(motorAddr)+' install limit switch home:'+str(homePos)+' Dist:'+str(lrDistance)+' limit:'+str(limitMin)+' , '+str(limitMax)+'\n')            

def print_driverList():
    print("| --- Driver List ---")
    for item in driverDict.items():
        print("| {0:10s} : {1:14s} |".format(item[0],item[1]))

def main():
    print("[Stepper Install]Start")
    agvs = sys.argv
    argc = len(agvs)

    # stepper_install.py PR0_GAS
    prefix = sys.argv[1] 
    sus,part,motor=prefix.split('_')
    motortype, model=sus.split('-')
    drivername = model + '_' + part
    #print prefix
    #print sus,part,motor,motortype,model, drivername

    if (argc != 2):
        print('! stepper_install (DRIVER_NAME)_(MOTOR)')
        print(' ex. stepper_install K1:STEPPER-BS_GAS_0 [0 to 5]')
        print(' ex. stepper_install K1:STEPPER-BS_IP_A [0:A,1:B,2:C,3:F0Y]')
        print_driverList()        
        quit()
    if drivername not in driverDict:
        print('! please check DRIVER_NAME %s' % drivername)
        print_driverList()
        quit()

    driverIP = driverDict[drivername]
    print(driverIP)

    if part == 'GAS':
        motorAddr = int(motor)
        print('GAS initilize started')
    elif part == 'IP':
        motorAddr  = conf.channel[drivername]['motor'+motor[0]]
        print('IP initilize started motor'+motor, motorAddr)

#    os.chdir('/opt/rtcds/userapps/release/cds/common/scripts/epics-motor-control/stepmotor')
    driver = Trinamic_control6110()
    driver.connectTCP(driverIP, 4001)
    driver.reconnect()

    initialize(driver,motorAddr,prefix)
    driver.close()
    #exit()
    print("[Stepper Install]Complete!")

if __name__ == '__main__':
    main()    
