#!/usr/bin/env python3
#! coding:utf-8
'''
    Picomotor Power Control
    MEIKO WATCH BOOT nino RPC-MCS

    Usage:
        pico_power_control.py [TARGET] [ON or OFF]
        ex.
            pico_power_controls.py TEST ON
'''
import sys
import getpass
import telnetlib
import time
import subprocess
from datetime import datetime
from datetime import timedelta

driverDict = {
    # Same happy_pico_start.py list.
    #"MCO"      :{"IPADDR":"10.68.160.101", "OUTLET":1}, # MCF
    #"STM1"     :{"IPADDR":"10.68.160.90", "OUTLET":1}, 
    #"STM2"     :{"IPADDR":"10.68.160.90", "OUTLET":1}, 
    #"POM1"     :{"IPADDR":"10.68.160.90", "OUTLET":1}, 
    "MCF"      :{"IPADDR":"10.68.160.101", "OUTLET":1},  
    "MCE"      :{"IPADDR":"10.68.160.102", "OUTLET":1},  
    "IMMT1"    :{"IPADDR":"10.68.160.103", "OUTLET":1}, 
    "IMMT2"    :{"IPADDR":"10.68.160.104", "OUTLET":1}, 
    "PR3_IM"   :{"IPADDR":"10.68.160.105", "OUTLET":1}, 
    "PR3_BF"   :{"IPADDR":"10.68.160.105", "OUTLET":2}, 
    "PR2_IM"   :{"IPADDR":"10.68.160.106", "OUTLET":1}, 
    "PR2_BF"   :{"IPADDR":"10.68.160.106", "OUTLET":2}, 
    "PRM_IM"   :{"IPADDR":"10.68.160.107", "OUTLET":1}, 
    "PRM_BF"   :{"IPADDR":"10.68.160.107", "OUTLET":2}, 
    "BS_IM"    :{"IPADDR":"10.68.160.108", "OUTLET":1}, 
    "BS_BF"    :{"IPADDR":"10.68.160.108", "OUTLET":2}, 
    "SR3_IM"   :{"IPADDR":"10.68.160.109", "OUTLET":1}, 
    "SR3_BF"   :{"IPADDR":"10.68.160.109", "OUTLET":2}, 
    "SR2_IM"   :{"IPADDR":"10.68.160.110", "OUTLET":1}, 
    "SR2_BF"   :{"IPADDR":"10.68.160.110", "OUTLET":2}, 
    "SRM_IM"   :{"IPADDR":"10.68.160.111", "OUTLET":1}, 
    "SRM_BF"   :{"IPADDR":"10.68.160.111", "OUTLET":2}, 
    "ETMX"     :{"IPADDR":"10.68.160.112", "OUTLET":1}, 
    "ETMY"     :{"IPADDR":"10.68.160.113", "OUTLET":1}, 
    "ITMX"     :{"IPADDR":"10.68.160.114", "OUTLET":1}, 
    "ITMY"     :{"IPADDR":"10.68.160.115", "OUTLET":1}, 
    "OMMT1"    :{"IPADDR":"10.68.160.116", "OUTLET":1}, 
    "OMMT2"    :{"IPADDR":"10.68.160.116", "OUTLET":2}, 
    "OSTM"     :{"IPADDR":"10.68.160.117", "OUTLET":1}, 
    "PCAL_EX1" :{"IPADDR":"10.68.160.118", "OUTLET":1}, 
    "PCAL_EX2" :{"IPADDR":"10.68.160.118", "OUTLET":2}, 
    "PCAL_EY1" :{"IPADDR":"10.68.160.119", "OUTLET":1}, 
    "PCAL_EY2" :{"IPADDR":"10.68.160.119", "OUTLET":2}, 
    "POP"      :{"IPADDR":"10.68.160.120", "OUTLET":1}, 
    "POS"      :{"IPADDR":"10.68.160.121", "OUTLET":1}, 
    "TEST"     :{"IPADDR":"10.68.150.90", "OUTLET":1}, 
    "TEST2"     :{"IPADDR":"10.68.150.90", "OUTLET":2}, 
    "TEST3"     :{"IPADDR":"10.68.160.109", "OUTLET":1}, 
    #"AS_WFS"   :{"IPADDR":"Use SmartPlag", "OUTLET":1}, 
    #"REFL_WFS" :{"IPADDR":"Use SmartPlag", "OUTLET":1}, 
}

cmdListDic={
    "ON":'PON',
    "OFF":'POF',
    "REBOOT":'POR',
}

TIMEOUT = 60

def print_driverList():
    print("| --- Driver List ---")
    for item in driverDict.items():
        print("| {0:10s} : {1:14s} |".format(item[0],item[1]['IPADDR']))

class rpcm2cs_telnet(object):
    def __init__(self,prefix,host,timeout):
        self.prefix = prefix
        self.host = host
        self.port = 23
        self.timeout = timeout
        self.logfile = '/kagra/Dropbox/Subsystems/VIS/Scripts/PicoMotorPowerController/LogFiles/'+self.prefix+'.log'

        self.connect()
  
    def connect(self):
        try:
            print('Connecting to ',self.host)
            self.tn=telnetlib.Telnet(self.host,port=self.port, timeout=self.timeout)
            self.logOutput('Conecting to: '+self.host)

        except:
            print('! Not Connected %s' % self.host)
            self.logOutput('Not Conected to: '+self.host)

            quit()

    def read_until(self,readdata):
        try:
            #print(readdata)
            return self.tn.read_until(readdata,self.timeout)
        except:
            print('Error: Not Read Data %s' % readdata)
            quit()

    def write(self,writedata):
        try:
            #print(writedata)
            self.tn.write(writedata)
        except:
            print('Error: Not Write Data %s' % writedata)
            quit()

    '''
        Login
    '''
    def login(self):
        user='pico'
        password='P0wer0n'
        self.read_until(b"220 RPC-M2CS (Noname) server ready.")

        self.write(b'\r\n')
        self.read_until(b"ID:")
        self.write(user.encode('ascii')+b"\r\n")
        self.read_until(b"Password:")
        self.write(password.encode('ascii')+b'\r\n')
        self.read_until(b">")

    '''
        Logout
        Send command
            Q : Logout telenet
    '''
    def logout(self):
        self.write(b'Q\r\n')
        self.logOutput('Logout of: '+self.host)

    '''
        Get Outret State
        Send command
            POS : Get Outret State
        Result
            Power State 
            00 : Outlet 1 and 2 power off
            10 : Outlet 1 Power On and Outlet 2 power off
            01 : Outlet 1 Power Off and Outlet 2 power on
            11 : Outlet 1 and 2 power on
    '''
    def getpos(self):
        self.write(b'POS\r\n')
        self.read_until(b"POS ")
        outlet = self.read_until(b"\r")
        self.read_until(b">")

        self.logOutput('Status:'+str(outlet[0:2]))

        return outlet

    '''
        Wait Outret State Change
        Send command
            XPOS : Get Outret State
    '''
    def getxpos(self):
        self.write(b'XPOS\r\n')
        self.read_until(b"XPOS ")
        status = self.read_until(b"\r")
        self.read_until(b">")

        zero = '0'
        cnt = 0
        while status[1:2] != zero.encode():
            self.write(b'XPOS\r\n')
            self.read_until(b"XPOS ")
            status = self.read_until(b"\r")
            self.read_until(b">")

            time.sleep(1)
            cnt += 1
            if cnt >= 30:
                print("Error: loop limit exceeded.",cnt)
                break

        cnt = 0
        while status[8:9] != zero.encode():
            self.write(b'XPOS\r\n')
            self.read_until(b"XPOS ")
            status = self.read_until(b"\r")
            self.read_until(b">")

            time.sleep(1)
            cnt += 1
            if cnt >= 30:
                print("Error: loop limit exceeded.",cnt)
                break
            
        return status

    '''
        Turnon or off
        Send command
            PON1 or PON2 : Turn on Outret 1 or 2
            POF1 or POF2 : Turn off Outret 1 or 2
    '''
    def putTurnOnOff(self,cmd,outlet):
        cmd = cmd+str(outlet)
        self.write(bytes(cmd+'\r\n', encoding='utf-8'))
        self.logOutput('Send '+cmd)
        self.read_until(b">")

    '''
        Log File Output
    '''
    def logOutput(self,message):
        d = datetime.now()
        with open(self.logfile,'a') as f:
            f.write(d.strftime('%Y-%m-%d %H:%M:%S')+' '+message+'\n')

def main():
    agvs = sys.argv
    argc = len(agvs)

    print(sys.version_info)
    if(argc != 3):
        print_driverList()
        quit()
    if agvs[1] not in driverDict:
        print('! please check DRIVER_NAME %s' % agvs[1])
        print_driverList()
        quit()
    if agvs[2] not in cmdListDic:
        print('! please check Command %s' % agvs[2])
        print_driverList()
        quit()

    prefix =  agvs[1]
    host = driverDict[agvs[1]]['IPADDR']
    outlet = driverDict[agvs[1]]['OUTLET']

    drv = rpcm2cs_telnet(prefix, host, TIMEOUT)
    drv.login()
    drv.getpos()    # Write Log
    drv.putTurnOnOff(cmdListDic[agvs[2]],outlet)   # Turn On command works with delay.
    drv.getxpos()
    drv.logout()

    command = [
    'zenity'
    ,'--info'
    ,'--title=Result'
    ,'--width=300'
    ,'--timeout=5'
    ,'--text=\rThe restart process completed Successfully\r'
    ]
    print(command)
    subprocess.Popen(command)

if __name__== "__main__":
    main()
