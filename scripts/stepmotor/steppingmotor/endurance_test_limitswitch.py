from Trinamic_control6110 import *
import time

class EnduranceTest:
    def __init__(self, driver):

        self.driver = driver

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

        self.driver.setRightLimitSwitchEnable(True, 0)
        self.driver.setLeftLimitSwitchEnable(True,  0)
        self.driver.setRightLimitSwitchEnable(True, 1)
        self.driver.setLeftLimitSwitchEnable(True,  1)
        self.driver.setRightLimitSwitchEnable(True, 2)
        self.driver.setLeftLimitSwitchEnable(True,  2)
        self.driver.setRightLimitSwitchEnable(True, 3)
        self.driver.setLeftLimitSwitchEnable(True,  3)
        self.driver.setRightLimitSwitchEnable(True, 4)
        self.driver.setLeftLimitSwitchEnable(True,  4)
        self.driver.setRightLimitSwitchEnable(True, 5)
        self.driver.setLeftLimitSwitchEnable(True,  5)

    def start_atonece(self,motorAddr, toleft):
        self.driver.stop(motorAddr)
        self.driver.stop(motorAddr)
        self.driver.stop(motorAddr)
        self.driver.stop(motorAddr)
        
        isError = False

        # Move in forward.
        if toleft == True:
            step = 1000000
            rswitch_target = 1
            lswitch_target = 0
            move_dir = 'Left'
        else:
            step = -1000000
            rswitch_target = 0
            lswitch_target = 1
            move_dir = 'Right'
        print('Move in '+move_dir+': start ',step)

        pos =  self.driver.getActualPosition(motorAddr)
        self.driver.setTargetPosition(pos+step, motorAddr)        

        isError = self.check_moving_motor(motorAddr, 60)
        if isError:
            return isError

        # Check LR switch.      
        rswitch = self.driver.getRightLimitSwitch(motorAddr)
        lswitch = self.driver.getLeftLimitSwitch(motorAddr)
        print('- rswitch:',rswitch,' switch:',lswitch)
        if rswitch != rswitch_target:
            print('Error rswitch state:',rswitch,' target:',rswitch_target)
            isError = True
        if lswitch != lswitch_target:
            print('Error lswitch state:',lswitch,' target:',lswitch_target)
            isError = True
        if isError == True:
            print('Move in '+move_dir+': Error.')
            return isError
        else:
            print('Move in '+move_dir+': OK.')

        # Moving to reverse.
        if toleft == True:
            step = -1000
            move_dir = 'reverse right'
        else:
            step = 1000
            move_dir = 'reverse left'
        print('Move in '+move_dir+': start ',step)

        rswitch_target = 0
        lswitch_target = 0

        pos =  self.driver.getActualPosition(motorAddr)
        self.driver.setTargetPosition(pos+step, motorAddr)        

        isError = self.check_moving_motor(motorAddr, 10)
        if isError:
            return isError
        
        # Check LR switch.      
        rswitch = self.driver.getRightLimitSwitch(motorAddr)
        lswitch = self.driver.getLeftLimitSwitch(motorAddr)
        print('- rswitch:',rswitch,' switch:',lswitch)
        if rswitch != rswitch_target:
            print('Error rswitch state:',rswitch,'target:',rswitch_target)
            isError = True
        if lswitch != lswitch_target:
            print('Error lswitch state:',lswitch,'target:',lswitch_target)
            isError = True
            
        if isError == True:
            print('Move in '+move_dir+': Error.')
        else:
            print('Move in '+move_dir+': OK.')
        return isError
    
    def check_moving_motor(self,motorAddr,sleeptime):
        isError = False
        count = sleeptime
        while True:
            time.sleep(1)
            actualSpeed = self.driver.getActualSpeed(motorAddr)
            if actualSpeed == 0:
                break
            if count == 0:
                print('Error: Time Out')
                isError = True
                break
            count = count - 1
        return isError

    def stop(self,motorAddr):
        self.driver.stop(motorAddr)

if __name__ == '__main__':
    driver = Trinamic_control6110()
    driver.connectTCP('10.68.150.63', 4001)
    driver.reconnect()

    enduranceTest = EnduranceTest(driver)
    motorAddr = 0

    try:
        for i in range(100):
            print i+1,'/ 100 count'
            start = time.time()
            toLeft = True
            isError = enduranceTest.start_atonece(motorAddr,toLeft)
            if isError == True:
                enduranceTest.stop(motorAddr)
                break

            toLeft = False
            isError = enduranceTest.start_atonece(motorAddr,toLeft)
            if isError == True:
                enduranceTest.stop(motorAddr)
                break
            print('Motor Cooling at 10 sec! ')
            enduranceTest.stop(motorAddr)
            time.sleep(10)
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

        driver.close()

    except Exception, e:
        driver.close()
