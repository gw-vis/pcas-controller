#!/usr/bin/env python3
#! coding:utf-8

'''
    Document: JGW-G2112505
    ch.1: Pich(HR Side). Normal Use.
    ch.2: Roll.
    Ch.3: Pitch(AR Side).Used when Ch.1 is not moving.
'''

import sys,subprocess,os

driverDict = {
    "ETMY":"10.68.150.59",
    "ETMX":"10.68.150.60",
    "ITMY":"10.68.150.61",
    "ITMX":"10.68.150.62",
    "TEST":"10.68.150.63",
}

def print_driverList():
    print ("| --- Driver List ---|")
    for item in driverDict.items():
        print ("| {0:10s} : {1:14s} |".format(item[0],item[1]))
        
def main():
    agvs = sys.argv
    argc = len(agvs)

    killProcess = False
    if(argc == 3 and agvs[2]=='-kill'):
        killProcess = True

    if (argc != 2) and (killProcess == False):
        print ('! phytron_start (DRIVER_NAME)')
        print ('! phytron_start (DRIVER_NAME) -kill')
        print_driverList()        
        quit()
    if agvs[1] not in driverDict:
        print ('! please check DRIVER_NAME %s' % agvs[1])
        print_driverList()
        quit()

    #print "Exterminate !!!!!"
    #exit()
    os.chdir('/opt/rtcds/userapps/release/cds/common/scripts/epics-motor-control/phytron')
    command = 'python3 -m phytron K1:PHY-%s_ %s &' % (agvs[1],driverDict[agvs[1]])
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
        print (e)
        print ('Detect keyboard interrupt. Bye!')
        exit()    
