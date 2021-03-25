#!/usr/bin/env python3
#! coding:utf-8
"""
 modified in Feb 3 2018.
 A. Shoda
"""

#import sys,commands,os
import sys,os
import subprocess

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
    "TEST_IP"   :"10.68.150.63"
}

def print_driverList():
    print("| --- Driver List ---")
    for item in driverDict.items():
        print("| {0:10s} : {1:14s} |".format(item[0],item[1]))
        
def main():
    agvs = sys.argv
    argc = len(agvs)

    killProcess = False
    if(argc == 3 and agvs[2]=='-kill'):
        killProcess = True

    if (argc != 2) and (killProcess == False):
        print('! step_start (DRIVER_NAME)')
        print('! step_start (DRIVER_NAME) -kill')
        print_driverList()        
        print(sys.version_info)
        quit()
    if agvs[1] not in driverDict:
        print('! please check DRIVER_NAME %s' % agvs[1])
        print_driverList()
        print(sys.version_info)
        quit()

    #print "Exterminate !!!!!"
    #exit()
    if 'k1script1' in os.uname()[1]:
        print('k1script1 is Python3')
        command = 'python3 -m picomotor K1:PICO-%s_ %s &' % (agvs[1],driverDict[agvs[1]])
    else:
        print('Please run it from k1script1')
        print('$> ssh k1script1')
        print('$> step_start (SERVER_NAME)')
        quit()

    os.chdir('/opt/rtcds/userapps/release/cds/common/scripts/epics-motor-control/stepmotor')
#    os.chdir('/users/ikeda/Git/pcas-controller/scripts/stepmotor')
#    print(os.path.dirname(os.path.abspath(__file__)))
#    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print('python3 -m steppingmotor K1:STEPPER-%s_ %s &' % (agvs[1],driverDict[agvs[1]]))
#    os.system('python -m steppingmotor K1:STEPPER-%s_ %s &' % (agvs[1],driverDict[agvs[1]]) )
    command = 'python3 -m steppingmotor K1:STEPPER-%s_ %s' % (agvs[1],driverDict[agvs[1]])

    pid = process_check(command)
    if pid != 0 and killProcess == True:
        process_kill(pid)

    if pid == 0 and killProcess == False:
        subprocess.Popen(command.split())

def process_check(cmdline):
    cmd = ['ps xo pid,args']
    proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)

    for line in proc.stdout:
        strline=str(line.decode(encoding='utf-8'))
        pid = strline[:5]
        args= strline[6:-1]
        if args == cmdline:
            return int(pid)
    return 0

def process_kill(pid):
    cmd = ['kill '+str(pid)]
    print(cmd)
    proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)


if __name__ == "__main__":
    main()    
