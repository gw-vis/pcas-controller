#!/usr/bin/env python3

header = '''
file {
	name="/opt/rtcds/userapps/release/cds/common/medm/picomotor/OVERVIEW/HAPPY_PICO_OVERVIEW_BAK.adl"
	version=030109
}
display {
	object {
		x=2570
		y=108
		width=1000
		height=700
	}
	clr=14
	bclr=11
	cmap=""
	gridSpacing=5
	gridOn=0
	snapToGrid=0
}
"color map" {
	ncolors=65
	colors {
		ffffff,
		ececec,
		dadada,
		c8c8c8,
		bbbbbb,
		aeaeae,
		9e9e9e,
		919191,
		858585,
		787878,
		696969,
		5a5a5a,
		464646,
		2d2d2d,
		000000,
		00d800,
		1ebb00,
		339900,
		2d7f00,
		216c00,
		fd0000,
		de1309,
		be190b,
		a01207,
		820400,
		5893ff,
		597ee1,
		4b6ec7,
		3a5eab,
		27548d,
		fbf34a,
		f9da3c,
		eeb62b,
		e19015,
		cd6100,
		ffb0ff,
		d67fe2,
		ae4ebc,
		8b1a96,
		610a75,
		a4aaff,
		8793e2,
		6a73c1,
		4d52a4,
		343386,
		c7bb6d,
		b79d5c,
		a47e3c,
		7d5627,
		58340f,
		99ffff,
		73dfff,
		4ea5f9,
		2a63e4,
		0a00b8,
		ebf1b5,
		d4db9d,
		bbc187,
		a6a462,
		8b8239,
		73ff6b,
		52da3b,
		3cb420,
		289315,
		1a7309,
	}
}
rectangle {
	object {
		x=490
		y=366
		width=220
		height=70
	}
	"basic attribute" {
		clr=57
	}
}
rectangle {
	object {
		x=2
		y=471
		width=200
		height=200
	}
	"basic attribute" {
		clr=57
	}
}
rectangle {
	object {
		x=2
		y=366
		width=115
		height=100
	}
	"basic attribute" {
		clr=57
	}
}
text {
	object {
		x=497
		y=369
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="All IM chans"
}
text {
	object {
		x=515
		y=385
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="1: PITCH"
}
text {
	object {
		x=515
		y=401
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="2: ROLL"
}
text {
	object {
		x=516
		y=417
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="3: YAW"
}
text {
	object {
		x=6
		y=369
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="IMMTs1&2 chans"
}
text {
	object {
		x=10
		y=385
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="1: PITCH"
}
text {
	object {
		x=10
		y=399
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="2: YAW"
}
text {
	object {
		x=11
		y=429
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="4: Y"
}
text {
	object {
		x=10
		y=414
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="3: X(optical axis)"
}
rectangle {
	object {
		x=369
		y=445
		width=150
		height=240
	}
	"basic attribute" {
		clr=57
	}
}
text {
	object {
		x=387
		y=447
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="PICO EFFICIENCIES"
}
text {
	object {
		x=395
		y=460
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="UNIT: urad / STEP"
}
text {
	object {
		x=372
		y=501
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="ETMX"
}
text {
	object {
		x=413
		y=502
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  -0.198"
}
text {
	object {
		x=417
		y=480
		width=150
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="A    B   YAW"
}
text {
	object {
		x=15
		y=474
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="PICO EFFICIENCIES"
}
text {
	object {
		x=9
		y=524
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="MCO"
}
text {
	object {
		x=52
		y=524
		width=100
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="+3.0   +0.2"
}
text {
	object {
		x=27
		y=490
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="UNIT: urad / STEP"
}
text {
	object {
		x=53
		y=508
		width=100
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PITCH  YAW"
}
text {
	object {
		x=9
		y=543
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="MCI"
}
text {
	object {
		x=52
		y=543
		width=100
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="+1.0   -0.05"
}
text {
	object {
		x=9
		y=562
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="MCE"
}
text {
	object {
		x=53
		y=562
		width=100
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="-0.1   -0.05"
}
text {
	object {
		x=9
		y=581
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="IMMT1"
}
text {
	object {
		x=53
		y=581
		width=100
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="+0.5   -0.05"
}
text {
	object {
		x=9
		y=600
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="IMMT2"
}
text {
	object {
		x=53
		y=600
		width=100
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="-0.5   -0.05"
}
text {
	object {
		x=605
		y=370
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="All BF chans"
}
text {
	object {
		x=622
		y=388
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="1: PITCH(L)"
}
text {
	object {
		x=622
		y=404
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="2: ROLL(T)"
}
rectangle {
	object {
		x=370
		y=366
		width=115
		height=70
	}
	"basic attribute" {
		clr=57
	}
}
text {
	object {
		x=375
		y=369
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="All TypeA chans"
}
text {
	object {
		x=376
		y=385
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="1: Mooving mass A"
}
text {
	object {
		x=376
		y=401
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="2: Mooving mass B"
}
text {
	object {
		x=376
		y=417
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="3: BF YAW"
}
rectangle {
	object {
		x=526
		y=445
		width=180
		height=240
	}
	"basic attribute" {
		clr=57
	}
}
text {
	object {
		x=544
		y=448
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="PICO EFFICIENCIES"
}
text {
	object {
		x=552
		y=461
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="UNIT: urad / STEP"
}
text {
	object {
		x=530
		y=655
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PRM_BF"
}
text {
	object {
		x=530
		y=638
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PRM_IM"
}
text {
	object {
		x=529
		y=589
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PR2_BF"
}
text {
	object {
		x=529
		y=604
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PR3_IM"
}
text {
	object {
		x=578
		y=604
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="+0.05   0.04  -0.5"
}
text {
	object {
		x=529
		y=573
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PR2_IM"
}
text {
	object {
		x=529
		y=620
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PR3_BF"
}
text {
	object {
		x=578
		y=574
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="+0.05  ---  ---"
}
text {
	object {
		x=581
		y=655
		width=71
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="+     -"
}
text {
	object {
		x=578
		y=638
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="+0.03  +0.03  -0.22"
}
text {
	object {
		x=581
		y=475
		width=150
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PITCH  ROLL YAW"
}
text {
	object {
		x=372
		y=516
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="ETMY"
}
text {
	object {
		x=413
		y=517
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=372
		y=532
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="ITMX"
}
text {
	object {
		x=413
		y=533
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  -0.2"
}
text {
	object {
		x=372
		y=546
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="ITMY"
}
text {
	object {
		x=413
		y=547
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=371
		y=605
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="BS_IM"
}
text {
	object {
		x=371
		y=622
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="BS_BF"
}
text {
	object {
		x=371
		y=639
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="SR2_IM"
}
text {
	object {
		x=371
		y=656
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="SR2_BF"
}
text {
	object {
		x=529
		y=495
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="SR3_IM"
}
text {
	object {
		x=529
		y=511
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="SR3_BF"
}
text {
	object {
		x=529
		y=527
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="SRM_IM"
}
text {
	object {
		x=529
		y=544
		width=71
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="SRM_BF"
}
text {
	object {
		x=408
		y=585
		width=150
		height=16
	}
	"basic attribute" {
		clr=20
	}
	textix="PITCH  ROLL YAW"
}
text {
	object {
		x=415
		y=604
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=415
		y=619
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=415
		y=638
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=415
		y=657
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=579
		y=493
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=579
		y=508
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=580
		y=525
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=580
		y=541
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=578
		y=589
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
text {
	object {
		x=579
		y=620
		width=150
		height=16
	}
	"basic attribute" {
		clr=24
	}
	textix="---  ---  ---"
}
'''


#common = '/opt/rtcds/userapps/release/vis/common'
common = './'

def top(x,y):
    width = 300
    height = 120
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=30
    }}
    "composite name"=""
    "composite file"="./OVERVIEW_TOP.adl"
    }}
    '''.format(common=common,x=x,y=y)
    return txt,width,height


def mini(x,y,picoid,picoid_label,ch1,ch2,ch3,ch4,pwctl,optics,pico_pos_yaml,sensor_yaml,ch1_yaml,ch2_yaml,ch3_yaml,ch4_yaml,dof1,dof2,dof3,dof4,sensor_label,ndscope):
    width = 120
    height = 30
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=30
    }}
    "composite name"=""
    "composite file"="./HAPPY_PICO_MINI.adl;IFO=$(IFO),PICOID={picoid},PICOID_LABEL={picoid_label},CH1={ch1},CH2={ch2},CH3={ch3},CH4={ch4},PWCTL={pwctl},OPTICS={optics},PICO_POS_YAML={pico_pos_yaml},SENSOR_YAML={sensor_yaml},CH1_YAML={ch1_yaml},CH2_YAML={ch2_yaml},CH3_YAML={ch3_yaml},CH4_YAML={ch4_yaml},DOF1={dof1},DOF2={dof2},DOF3={dof3},DOF4={dof4},SENSOR_LABEL={sensor_label},NDSCOPE={ndscope}"
    }}
    '''.format(common=common,x=x,y=y,picoid=picoid,picoid_label=picoid_label,ch1=ch1,ch2=ch2,ch3=ch3,ch4=ch4,pwctl=pwctl,optics=optics,pico_pos_yaml=pico_pos_yaml,sensor_yaml=sensor_yaml,ch1_yaml=ch1_yaml,ch2_yaml=ch2_yaml,ch3_yaml=ch3_yaml,ch4_yaml=ch4_yaml,dof1=dof1,dof2=dof2,dof3=dof3,dof4=dof4,sensor_label=sensor_label,ndscope=ndscope)
    return txt,width,height

def head(x,y,system,mtype):
    width = 300
    height = 50
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=30
    }}
    "composite name"=""
    "composite file"="./HEAD_MINI.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},TYPE={mtype}"
    }}
    '''.format(common=common,x=x,y=y,system=system,mtype=mtype)
    return txt,width,height

def foot(x,y,stepperid,systems,vacsystem,ip_lvdtinf_yaml,ip_damp_yaml,gas_damp_yaml,ip_stepper_yaml,gas_stepper_yaml,ip_stepper_limit_yaml,gas_stepper_limit_yaml):
    width = 300
    height = 50
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=30
    }}
    "composite name"=""
    "composite file"="./FOOT_MINI.adl;IFO=$(IFO),ifo=$(ifo),STEPPERID={stepperid},OPTICS={system},VACOPTICS={vacsystem},ip_lvdtinf_yaml={ip_lvdtinf_yaml},ip_damp_yaml={ip_damp_yaml},gas_damp_yaml={gas_damp_yaml},ip_stepper_yaml={ip_stepper_yaml},gas_stepper_yaml={gas_stepper_yaml},ip_stepper_limit_yaml={ip_stepper_limit_yaml},gas_stepper_limit_yaml={gas_stepper_limit_yaml}"
    }}
    '''.format(common=common,x=x,y=y,stepperid=stepperid,system=system,vacsystem=vacsystem,ip_lvdtinf_yaml=ip_lvdtinf_yaml,ip_damp_yaml=ip_damp_yaml,gas_damp_yaml=gas_damp_yaml,ip_stepper_yaml=ip_stepper_yaml,gas_stepper_yaml=gas_stepper_yaml,ip_stepper_limit_yaml=ip_stepper_limit_yaml,gas_stepper_limit_yaml=gas_stepper_limit_yaml)
    return txt,width,height

def pwctl_is(system):
    if pwctls[system] == True:
        return 'PWCTL'
    return 'NO_PWCTL'

if __name__=='__main__':
#    systems = ['MCF', 'MCE', 'STMs', 'IMMT1', 'IMMT2', 'POP_POM', 'POS_POM', 'OMMT1', 'OMMT2', 'OSTM', 'PR3_IM', 'PR3_BF', 'PR2_IM', 'PR2_BF', 'PRM_IM', 'PRM_BF', 'PCAL_EX1', 'PCAL_EY1', 'PCAL_EX2', 'PCAL_EY2', 'ETMX', 'ETMY', 'ITMX', 'ITMY', 'BS_IM', 'BS_BF', 'SR2_IM', 'SR2_BF', 'SR3_IM', 'SR3_BF', 'SRM_IM', 'SRM_BF', 'REFL_WFS', 'AS_WFS']
    displist = ['MC', 'Table', 'OMC', 'Type-A', 'Type-B', 'Type-Bp', 'PCAL', 'TEST']
    displayitems = {'MC': ['MCF', 'MCE', 'STMs', 'IMMT1', 'IMMT2'],
                  'Table': ['POP_POM', 'POS_POM', 'REFL_WFS', 'AS_WFS'],
                  'OMC': ['OMMT1', 'OMMT2', 'OSTM'],
                  'Type-A': ['ETMX', 'ETMY', 'ITMX', 'ITMY'],
                  'Type-B': ['BS_IM', 'BS_BF', 'SR2_IM', 'SR2_BF', 'SR3_IM', 'SR3_BF', 'SRM_IM', 'SRM_BF'],
                  'Type-Bp': ['PR2_IM', 'PR2_BF', 'PR3_IM', 'PR3_BF', 'PRM_IM', 'PRM_BF'],
                  'PCAL':  ['PCAL_EX1', 'PCAL_EX2', 'PCAL_EY1', 'PCAL_EY2'],
                  'TEST': ['TEST']
            }

    stages = {'MCF': ['MCO', 'MCO:PIT', 'MCO:YAW', 'MCI:PIT', 'MCI:YAW'],
              'MCE': ['MCE', 'MCE:PIT', 'MCE:YAW', 'MCE:3', 'MCE:4'],
              'STMs': ['MCI', 'MCI:1', 'MCI:2', 'MCI:3', 'MCI:4'],
              'IMMT1': ['IMMT1', 'IMMT1:PITCH', 'IMMT1:YAW', 'IMMT1:X', 'IMMT1:Y'],
              'IMMT2': ['IMMT2', 'IMMT2:PITCH', 'IMMT2:YAW', 'IMMT2:X', 'IMMT2:Y'],
              'POP_POM': ['POP_POM', 'POP_POM:AIR_P', 'POP_POM:AIR_Y', 'POP_POM:VAC_P', 'POP_POM:VAC_Y'],
              'POS_POM': ['POP_POM', 'POS_POM:AIR_P', 'POS_POM:AIR_Y', 'POS_POM:VAC_P', 'POS_POM:VAC_Y'],
              'OMMT1': ['OMMT1', 'OMMT1:PITCH', 'OMMT1:YAW', 'OMMT1:X', 'OMMT1:Y'],
              'OMMT2': ['OMMT2', 'OMMT2:PITCH', 'OMMT2:YAW', 'OMMT2:X', 'OMMT2:Y'],
              'OSTM': ['OSTM', 'OSTM:PITCH', 'OSTM:YAW', 'OSTM:X', 'OSTM:Y'],
              'PR3_IM': ['PR3_IM', 'PR3_IM:PITCH', 'PR3_IM:ROLL', 'PR3_IM:YAW', 'PR3_IM:None'],
              'PR3_BF': ['PR3_BF', 'PR3_BF:PITCH(L)', 'PR3_BF:ROLL(T)', 'PR3_BF:None', 'PR3_BF:None'],
              'PR2_IM': ['PR2_IM', 'PR2_IM:PITCH', 'PR2_IM:ROLL', 'PR2_IM:YAW', 'PR2_IM:4'],
              'PR2_BF': ['PR2_BF', 'PR2_BF:PITCH(L)', 'PR2_BF:ROLL(T)', 'PR2_BF:None', 'PR2_BF:None'],
              'PRM_IM': ['PRM_IM', 'PRM_IM:PITCH', 'PRM_IM:ROLL', 'PRM_IM:YAW', 'PRM_IM:None'],
              'PRM_BF': ['PRM_BF', 'PRM_BF:PITCH(L)', 'PRM_BF:ROLL(T)', 'PRM_BF:None', 'PRM_BF:None'],
              'PCAL_EX1': ['PCAL_EX1', 'PCAL_EX1:Lower(PITCH)','PCAL_EY1:Lower(YAW)', 'PCAL_EX1:Upper(PITCH)','PCAL_EX1:Upper(YAW)'],
              'PCAL_EY1': ['PCAL_EY1', 'PCAL_EY1:1','PCAL_EX1:2', 'PCAL_EY1:3', 'PCAL_EY1:4'],
              'PCAL_EX2': ['PCAL_EX2', 'PCAL_EX2:Lower(PITCH)','PCAL_EX2:Lower(YAW)', 'PCAL_EX2:Upper(PITCH)','PCAL_EX2:Upper(YAW)'],
              'PCAL_EY2': ['PCAL_EY2', 'PCAL_EY2:1','PCAL_EY2:2', 'PCAL_EY2:3', 'PCAL_EY2:4'],
              'ETMX': ['ETMX', 'ETMX:1', 'ETMX:2', 'ETMX:BF_Yaw', 'ETMX:None'],
              'ETMY': ['ETMY', 'ETMY:1', 'ETMY:2', 'ETMY:BF_Yaw', 'ETMY:None'],
              'ITMX': ['ITMX', 'ITMX:1', 'ITMX:2', 'ITMX:BF_Yaw', 'ITMX:None'],
              'ITMY': ['ITMY', 'ITMX:1', 'ITMX:2', 'ITMX:BF_Yaw', 'ITMX:None'],
              'BS_IM': ['BS_IM', 'BS_IM:PITCH', 'BS_IM:ROLL', 'BS_IM:YAW', 'BS_IM:None'],
              'BS_BF': ['BS_BF', 'BS_BF:PITCH', 'BS_BF:ROLL', 'BS_BF:None', 'BS_BF:None'],
              'SR2_IM': ['SR2_IM', 'SR2_IM:PITCH', 'SR2_IM:ROLL', 'SR2_IM:YAW', 'SR2_IM:4'],
              'SR2_BF': ['SR2_BF', 'SR2_BF:PITCH(L)', 'SR2_BF:ROLL(T)', 'SR2_BF:None', 'SR2_BF:None',],
              'SR3_IM': ['SR3_IM', 'SR3_IM:PITCH', 'SR3_IM:ROLL', 'SR3_IM:YAW', 'SR3_IM:4'],
              'SR3_BF': ['SR3_BF', 'SR3_BF:PITCH(L)', 'SR3_BF:ROLL(T)', 'SR3_BF:None', 'SR3_BF:None'],
              'SRM_IM': ['SRM_IM', 'SRM_IM:PITCH', 'SRM_IM:ROLL', 'SRM_IM:YAW', 'SRM_IM:4'],
              'SRM_BF': ['SRM_BF', 'SRM_BF:PITCH(L)', 'SRM_BF:ROLL(T)', 'SRM_BF:None', 'SRM_BF:None'],
              'REFL_WFS': ['REFL_WFS', 'REFL_WFS:1', 'REFL_WFS:2', 'REFL_WFS:3', 'REFL_WFS:4'],
              'AS_WFS': ['AS_WFS', 'AS_WFS:1', 'AS_WFS:2', 'AS_WFS:3', 'AS_WFS:4'],
              'TEST': ['TEST', 'TEST:1', 'TEST:2', 'TEST:3', 'TEST:4']
            }

    pwctls = {'MCF': True,
              'MCE': False,
              'STMs': False,
              'IMMT1':False,
              'BS': False,
              'IMMT2': False,
              'POP_POM': False,
              'POS_POM': False,
              'OMMT1': True,
              'OMMT2': True,
              'OSTM': True,
              'PR3_IM': True,
              'PR3_BF': True,
              'PR2_IM': True,
              'PR2_BF': True,
              'PRM_IM': True,
              'PRM_BF': True,
              'PCAL_EX1': True,
              'PCAL_EX2': True,
              'PCAL_EY1': True,
              'PCAL_EY2': True,
              'ETMX': True,
              'ETMY': True,
              'ITMX': True,
              'ITMY': True,
              'BS_IM': True,
              'BS_BF': True,
              'SR2_IM': True,
              'SR2_BF': True,
              'SR3_IM': True,
              'SR3_BF': True,
              'SRM_IM': True,
              'SRM_BF': True,
              'REFL_WFS': False,
              'AS_WFS': False,
              'TEST': False
            }
    yamlfile_path ='/opt/rtcds/userapps/trunk/cds/common/medm/picomotor/OVERVIEW/'
    yamlfile_pico_pos=yamlfile_path+'pico_pos.yml'
    yamlfile_im_damp_all=yamlfile_path+'im_damp_all.yml'
    yamlfile_im_damp=yamlfile_path+'im_damp.yml'

    yamlfile = {'MCF': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'MCE': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'STMs': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'IMMT1': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'IMMT2':  ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'POP_POM': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'POS_POM': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'OMMT1': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'OMMT2': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'OSTM': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'PR3_IM': ['PR3',yamlfile_pico_pos, yamlfile_im_damp_all, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, 'P', 'R', 'Y', 'None', 'IM_DAMP', 'ALL_NDSCOPE'],
                'PR3_BF': ['PR3',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'PR2_IM': ['PR2',yamlfile_pico_pos, yamlfile_im_damp_all, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, 'P', 'R', 'Y', 'None', 'IM_DAMP', 'ALL_NDSCOPE'],
                'PR2_BF': ['PR2',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'PRM_IM': ['PRM',yamlfile_pico_pos, yamlfile_im_damp_all, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, 'P', 'R', 'Y', 'None', 'IM_DAMP', 'ALL_NDSCOPE'],
                'PRM_BF': ['PRM',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'PCAL_EX1': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'PCAL_EY1': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'PCAL_EX2': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'PCAL_EY2': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'ETMX': ['ETMX',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'ETMY': ['ETMY',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'ITMX': ['ITMX',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'ITMY': ['ITMY',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'BS_IM': ['BS',yamlfile_pico_pos, yamlfile_im_damp_all, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, 'P', 'R', 'Y', 'None', 'IM_DAMP', 'ALL_NDSCOPE'],
                'BS_BF': ['BS',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'SR2_IM': ['SR2',yamlfile_pico_pos, yamlfile_im_damp_all, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, 'P', 'R', 'Y', 'None', 'IM_DAMP', 'ALL_NDSCOPE'],
                'SR2_BF': ['SR2',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'SR3_IM': ['SR3',yamlfile_pico_pos, yamlfile_im_damp_all, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, 'P', 'R', 'Y', 'None', 'IM_DAMP', 'ALL_NDSCOPE'],
                'SR3_BF': ['SR3',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'SRM_IM': ['SRM',yamlfile_pico_pos, yamlfile_im_damp_all, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, yamlfile_im_damp, 'P', 'R', 'Y', 'None', 'IM_DAMP', 'ALL_NDSCOPE'],
                'SRM_BF': ['SRM',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'REFL_WFS': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'AS_WFS': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                'TEST': ['None',yamlfile_pico_pos, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'SIMPLE_NDSCOPE'],
                }
    mode = 'ERR'
 
    height = 0
    width = 0
    _h0 = height
    _w0 = width
    contents = header
    _h = 0
    _w = 0
    with open('./HAPPY_PICO_OVERVIEW.adl','w') as f:
        txt,w0,h0 = top(width,height)
        contents += txt
        height += h0
        _h0 = height
        width = 10

        for disp in displist:
            systems = displayitems[disp]

            for system in systems:
                #print('{0}'.format(system))
            
    #            txt,w0,h0 = head(width,height,system,mtype)
    #            contents += txt         
    #            _h = h0
                pwctl = pwctl_is(system)
                txt,w1,h1 = mini(width,height+_h,stages[system][0],system,stages[system][1],stages[system][2],stages[system][3],stages[system][4],pwctl,
                                yamlfile[system][0],
                                yamlfile[system][1],yamlfile[system][2],yamlfile[system][3],yamlfile[system][4],yamlfile[system][5],
                                yamlfile[system][6],yamlfile[system][7],yamlfile[system][8],yamlfile[system][9],yamlfile[system][10],
                                yamlfile[system][11],yamlfile[system][12])
                _h += h1
                contents += txt

                print(system,pwctl)
    #            txt,w2,h2 = foot(width,height+_h,stepperid,system,vacsystem[system],yamlfile[system][0],yamlfile[system][1],yamlfile[system][2],yamlfile[system][3],yamlfile[system][4],yamlfile[system][5],yamlfile[system][6])
    #            contents += txt
    #            _h += h2 + 10
    #            _w = max(w0,w1,w2) +10
    #            q,mod = divmod(num+1,4)
    #            height = q*320 + _h0
    #            width = mod*_w + _w0
            height = _h0
            _h = 0
            width = width + w1

        f.write(contents)    
