#!/usr/bin/env python3
#! coding:utf-8
"""
 modified in Oct 3 2017.
 K. miyo
"""

#import sys,commands,os
import sys,os
import subprocess

driverDict = {
    "MCE"      :"10.68.150.22",
    "MCI"      :"10.68.150.3",
    "MCO"      :"10.68.160.4", # 20210629 Change(150->160)
    "STM1"     :"10.68.150.5",
    "STM2"     :"10.68.150.6",
    "POM1"     :"10.68.150.7",
    "IMMT1"    :"10.68.150.14",
    "IMMT2"    :"10.68.150.13",
    "PR2_BF"   :"10.68.160.12", # 20210701 Change(150->160)
    "PR2_IM"   :"10.68.160.15", # 20210701 Change(150->160)
    "PR3_BF"   :"10.68.160.10", # 20210628 Change(150->160)
    "PR3_IM"   :"10.68.160.11", # 20210628 Change(150->160)
    "PRM_BF"   :"10.68.160.8",  # 20210719 Change(150->160)
    "PRM_IM"   :"10.68.160.9",  # 20210719 Change(150->160)
    "BS_IM"    :"10.68.160.16", # 20210715 Change(150->160)
    "BS_BF"    :"10.68.160.17", # 20210715 Change(150->160)
    "ETMX"      :"10.68.150.20",
    "ETMY"      :"10.68.150.21",
    "ITMX"      :"10.68.150.18",
    "ITMY"      :"10.68.150.19",
    "SR2_IM"   :"10.68.160.24", # 20210630 Change(150->160)
    "SR2_BF"   :"10.68.160.25", # 20210630 Change(150->160)
    "SR3_IM"   :"10.68.160.26", # 20210618 Change(150->160)
    "SR3_BF"   :"10.68.160.27", # 20210618 Change(150->160)
    "SRM_IM"   :"10.68.160.32", # 20210709 Change(150->160)
    "SRM_BF"   :"10.68.160.23", # 20210709 Change(150->160)
#    "TEST"   :"10.68.150.22",    
    "POP_POM"   :"10.68.150.31",
    "POS_POM"   :"10.68.150.34",
    "PCAL_EX1"   :"10.68.150.35",
    "PCAL_EX2"   :"10.68.150.36",
    "PCAL_EY1"   :"10.68.150.37",
    "PCAL_EY2"   :"10.68.150.38",
    "OMMT1"   :"10.68.160.71",  # 20210622 Change(150->160)
    "OMMT2"   :"10.68.160.72",  # 20210622 Change(150->160)
    "OSTM"   :"10.68.160.73",   # 20210622 Change(150->160)
    "AS_WFS"   :"10.68.150.74",
    "REFL_WFS" :"10.68.150.75",
    "TEST" :"10.68.150.28",
#    "TEST" :"10.68.160.28",
}

def print_driverList():
    print("| --- Driver List ---")
    for item in driverDict.items():
        print("| {0:10s} : {1:14s} |".format(item[0],item[1]))
        
def main():
    agvs = sys.argv
    argc = len(agvs)

#    print(sys.version_info)
    killProcess = False
    if(argc == 3 and agvs[2]=='-kill'):
        killProcess = True

    if (argc != 2) and (killProcess == False):
        print('! pico_start (DRIVER_NAME)')
        print_driverList()        
        quit()
    if agvs[1] not in driverDict:
        print('! please check DRIVER_NAME %s' % agvs[1])
        print_driverList()
        quit()

    #print("Exterminate !!!!!")
    #exit()
    #os.chdir('/opt/rtcds/userapps/release/cds/common/scripts/picomotor')
    os.chdir('/opt/rtcds/userapps/release/cds/common/scripts/epics-motor-control/picomotor')
#    os.chdir('/users/ikeda/Git/pcas-controller/scripts/picomotor')

    if 'k1script1' in os.uname()[1]:
        print('k1script1 is Python3')
        command = 'python3 -m picomotor K1:PICO-%s_ %s &' % (agvs[1],driverDict[agvs[1]])
    elif 'k1script' in os.uname()[1]:
        print('k1script is Python2')
        command = 'python -m picomotor K1:PICO-%s_ %s &' % (agvs[1],driverDict[agvs[1]])
    else:
        print('Please run it from k1script1')
        print('$> ssh k1script1')
        print('$> happy_pico_start (DRIVER_NAME)')
        quit()

#    print(os.path.dirname(os.path.abspath(__file__)))
#    os.chdir(os.path.dirname(os.path.abspath(__file__)))
#    os.system('python3 -m picomotor K1:PICO-%s_ %s &' % (agvs[1],driverDict[agvs[1]]) )
    print(command)

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
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
        print('Detect keyboard interrupt. Bye!')
        exit()    
