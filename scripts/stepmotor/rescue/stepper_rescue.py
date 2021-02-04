#!/usr/bin/env python3
#! coding:utf-8
"""
 modified in Feb 3 2018.
 A. Shoda
"""
"""
Input: movestep, sleeptime, count

stepprt_rescue.py  ca, resolution(1:FULL,2:HALF,256:ustepx256), movestep, sleeptime]usec\, count
stepprt_rescue.py  SRM_GAS_2 1 2560 1000 10

"""
#import sys,commands,os
import sys,os
import subprocess
from epics import caget, caput, cainfo
import time

def caput_wap(ca,out):
    print('caput: ',ca,out)
    caput(ca,out)

def caget_wap(ca):
    res = caget(ca)
    print('caget: ',ca,res)
    return res

def main():
    direct_dic = {'FWD':1, 'REV':-1}
    agvs = sys.argv
    argc = len(agvs)

#    print(sys.version_info)
    if argc == 2:
        motor = agvs[1]
        print(motor)
        castr = 'K1:STEPPER-' + motor

#       motor = input('motor (ex.SRM_GAS_1):  > ')
#       resolution = int(input('resolution (ex. 0:FULL, 1:HALF, 8:ustepx256):  > '))

        vel = caget_wap(castr+'_VEL')
        resolution = caget_wap(castr+'_RESOLUTION')
        movestep = caget_wap(castr+'_FLUCTUATION')

        print('We got some values from the EPICS channel.')
        print('resolution:',resolution,' : 0:FULL, 1:HALF, 256:microstep')
        print('vel:',vel)
        print('movestep:',movestep)
        print('')
        print('Please enter some infomation.')

        direction = input('move directrion (ex. REV:<< or FWD:>> : ')
        if not direction in direct_dic:
            sys.exit(1)

        sleeptime = float(input('sleeptime [sec](ex.0.1): '))
        count_max = int(input('Repeat (ex.5): '))
        print('direction:',direction,' sleep time:',sleeptime,' loop count:',count_max)

    else:
        print('! stepprt_rescue.py SRM_GAS_2')
        sys.exit(1)

    judge = input('Can we initiate a rescue? y or n(other). > ')
    if judge != 'y':
        sys.exit(1)

    print('Start!')
    print('<< EMERGENCY stop Ctr+C >>')

    try:
        while True:
            for count in range(0,count_max):
                # moveing
                ut_st = time.time()
                caput_wap(castr+'_'+direction,1.0)

                pps = (16 * 1000000) / (8 * 2048 * 32) * float(vel)
                wait_time = movestep / pps
                print('wait:',wait_time,'pps:',pps)

                ut_mov_bef = time.time()
                time.sleep(wait_time) # sec
                ut_mov_aft = time.time()
                caput_wap(castr+'_STOP',1.0)
                #print(count,caget(castr+'_LOAD'))
                # wait
                ut_sleep_bef = time.time()
                time.sleep(sleeptime) # sec
                ut_sleep_aft = time.time()
                print('st-en:',ut_sleep_aft-ut_st,' mov:',ut_mov_aft-ut_mov_bef,' sleep:',ut_sleep_aft-ut_sleep_bef)

            print('Completed!')

            retry = input('Retry? y or n(other). > ')
            if retry != 'y':
                sys.exit(1)

    except KeyboardInterrupt:
        # Ctr-C
        print('Exception! Stop motor')
        caput_wap(castr+'_STOP',1.0)
        sys.exit(1)

if __name__ == "__main__":
    main()    
