#!/usr/bin/env python

header = '''
file {
	name="/opt/rtcds/userapps/release/cds/common/medm/steppingmotor/OFFLOAD_OVERVIEW/OFFLOAD_OVERVIEW.adl"
	version=030107
}
display {
	object {
		x=1996
		y=56
		width=1208
		height=651
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
'''

'''


TYPEA,ETMX,IP,GAS,
TYPEA,ITMX,IP,GAS,
TYPEA,ETMY,IP,GAS,
TYPEA,ITMY,IP,GAS,

    $(IFO):VIS-$(SYSTEM)_IP_SUMOUT_L_OUTPUT, T_OUTPUT, Y_OUTPUT, 
    $(IFO):VIS-$(SYSTEM)_F0_SUMOUT_GAS_OUTPUT, F1, F2, F3, BF
    IFO : K1
    SYSTEM : ETMX, ITMX, ETMY, ITMY

    MOTOR:
        $(IFO):STEPPER-(SYSTEM)_IP_L
        $(IFO):STEPPER-(SYSTEM)_GAS_(DOF)
        xx_IP: L:xx_IP_L T:xx_IP_T Y:xx_IP_Y
        ETMX_GAS: F0: ETMX_GAS_0 F1: ETMX_GAS_1 F2: ETMX_GAS_5 F3: ETMX_GAS_3 BF: ETMX-GAS_4
        ITMX_GAS: F0: ITMX_GAS_0 F1: ITMX_GAS_1 F2: ITMX_GAS_2 F3: ITMX_GAS_5 BF: ITMX-GAS_4
        ETMY_GAS: F0: ETMY_GAS_0 F1: ETMY_GAS_1 F2: ETMY_GAS_2 F3: ETMY_GAS_5 BF: ETMY-GAS_4
        ITMY_GAS: F0: ITMY_GAS_0 F1: ITMY_GAS_1 F2: ITMY_GAS_2 F3: ITMY_GAS_3 BF: ITMY-GAS_4

TYPEB,BS,IP,GAS,
TYPEB,SRM,IP,GAS,
TYPEB,SR2,IP,GAS,
TYPEB,SR3,IP,GAS,

    $(IFO):VIS-$(SYSTEM)_IP_SUMOUT_L_OUTPUT, T_OUTPUT, Y_OUTPUT, 
    $(IFO):VIS-$(SYSTEM)_F0_SUMOUT_GAS_OUTPUT, F1, F2, BF
    IFO : K1
    SYSTEM: BS, SRM, SR2, SR3
    MOTOR:
        xx_IP: L:xx_IP_L T:xx_IP_T Y:xx_IP_Y
        BS_GAS: F0: BS_GAS_3 F1: BS_GAS_1 BF: BS-GAS_0
        SR2_GAS: F0: SR2_GAS_2 F1: SR2_GAS_1 BF: SR2-GAS_0
        SR3_GAS: F0: SR3_GAS_2 F1: SR3_GAS_1 BF: SR3-GAS_0
        SRM_GAS: F0: SRM_GAS_3 F1: SRM_GAS_1 BF: SRM-GAS_0

TYPEBP,PRM,GAS,
TYPEBP,PR2,GAS,
TYPEBP,PR3,GAS,
    $(IFO):VIS-$(SYSTEM)_SF_SUMOUT_GAS_OUTPUT, BF
    IFO : K1
    SYSTEM: PRM, PR2, PR3
    MOTOR:
        PR2_GAS: BF: PR2_GAS_1, SF: PR2_GAS_2
        PR3_GAS: BF: PR0_GAS_0, SF: PR0_GAS_1
        PRM_GAS: BF: PR0_GAS_2, SF: PR0_GAS_3

'''
#common = '/opt/rtcds/userapps/release/vis/common'
common = './'

def usr_typea(x,y,system,F0,F1,F2,F3,BF):
    width = 300
    height = 320
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=320
    }}
    "composite name"=""
    "composite file"="./OFFLOAD_OVERVIEW_TYPEA.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},F0={f0},F1={f1},F2={f2},F3={f3},BF={bf}"
    }}
    '''.format(common=common,x=x,y=y,system=system,f0=F0,f1=F1,f2=F2,f3=F3,bf=BF)
    return txt,width,height
#    "composite file"="{common}/medm/steppingmotor/OFFLOAD_OVERVIEW/OFFLOAD_OVERVIEW_TYPEA.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},F0={f0},F1={f1},F2={f2},F3={f3},BF={bf}"

def usr_typeb(x,y,system,F0,F1,BF):
    width = 300
    height = 235
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=235
    }}
    "composite name"=""
    "composite file"="./OFFLOAD_OVERVIEW_TYPEB.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},F0={f0},F1={f1},BF={bf}"
    }}
    '''.format(common=common,x=x,y=y,system=system,f0=F0,f1=F1,bf=BF)
    return txt,width,height
#    "composite file"="{common}/medm/steppingmotor/OFFLOAD_OVERVIEW/OFFLOAD_OVERVIEW_TYPEA.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},F0={f0},F1={f1},F2={f2},F3={f3},BF={bf}"

def usr_typebp(x,y,system,SF,BF):
    width = 300
    height = 90
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=90
    }}
    "composite name"=""
    "composite file"="./OFFLOAD_OVERVIEW_TYPEBP.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},SF={sf},F={bf}"
    }}
    '''.format(common=common,x=x,y=y,system=system,sf=SF,bf=BF)
    return txt,width,height
#    "composite file"="{common}/medm/steppingmotor/OFFLOAD_OVERVIEW/OFFLOAD_OVERVIEW_TYPEA.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},F0={f0},F1={f1},F2={f2},F3={f3},BF={bf}"




if __name__=='__main__':
    systems = ['ETMX', 'ITMX', 'ETMY', 'ITMY', 'BS', 'SRM', 'SR2', 'SR3', 'PRM', 'PR2', 'PR3']
    #systems = ['TEST', 'TESTSR'] # TEST
    #systems = ['ETMX', 'ITMX', 'ETMY', 'ITMY']
    model = {
        'ETMX': {'Type': 'TypeA', 'CELL':{ 'colum':0, 'line':0 }, 'BS':{ 'F0':'ETMX_GAS_0', 'F1':'ETMX_GAS_1', 'F2':'ETMX_GAS_5', 'F3':'ETMX_GAS_3', 'BF':'ETMX_GAS_4'}},
        'ITMX': {'Type': 'TypeA', 'CELL':{ 'colum':1, 'line':0 }, 'BS':{ 'F0':'ETMX_GAS_0', 'F1':'ETMX_GAS_1', 'F2':'ETMX_GAS_2', 'F3':'ETMX_GAS_5', 'BF':'ETMX_GAS_4'}},
        'ETMY': {'Type': 'TypeA', 'CELL':{ 'colum':2, 'line':0 }, 'BS':{ 'F0':'ETMX_GAS_0', 'F1':'ETMX_GAS_1', 'F2':'ETMX_GAS_2', 'F3':'ETMX_GAS_5', 'BF':'ETMX_GAS_4'}},
        'ITMY': {'Type': 'TypeA', 'CELL':{ 'colum':3, 'line':0 }, 'BS':{ 'F0':'ETMX_GAS_0', 'F1':'ETMX_GAS_1', 'F2':'ETMX_GAS_2', 'F3':'ETMX_GAS_3', 'BF':'ETMX_GAS_4'}},

        'BS':  {'Type': 'TypeB', 'CELL':{ 'colum':0, 'line':1 }, 'BS':{ 'F0':'BS_GAS_3', 'F1':'BS_GAS_1', 'BF':'BS_GAS_0'}},
        'SR2': {'Type': 'TypeB', 'CELL':{ 'colum':2, 'line':1 }, 'BS':{ 'F0':'SR2_GAS_2', 'F1':'SR2_GAS_1', 'BF':'SR2_GAS_0'}},
        'SR3': {'Type': 'TypeB', 'CELL':{ 'colum':3, 'line':1 }, 'BS':{ 'F0':'SR3_GAS_2', 'F1':'SR3_GAS_1', 'BF':'SR3_GAS_0'}},
        'SRM': {'Type': 'TypeB', 'CELL':{ 'colum':1, 'line':1 }, 'BS':{ 'F0':'SRM_GAS_3', 'F1':'SRM_GAS_1', 'BF':'SRM_GAS_0'}},

        'PR2': {'Type': 'TypeBp', 'CELL':{ 'colum':1, 'line':2 }, 'BS':{ 'BF':'PR2_GAS_1', 'SF':'PR2_GAS_2'}},
        'PR3': {'Type': 'TypeBp', 'CELL':{ 'colum':2, 'line':2 }, 'BS':{ 'BF':'PRO_GAS_0', 'SF':'PRO_GAS_1'}},   # Motor !
        'PRM': {'Type': 'TypeBp', 'CELL':{ 'colum':0, 'line':2 }, 'BS':{ 'BF':'PR0_GAS_2', 'SF':'PR0_GAS_3'}},

        'TESTSR':  {'Type': 'TypeB', 'CELL':{ 'colum':0, 'line':0 }, 'BS':{ 'F0':'TEST_GAS_0', 'F1':'TEST_GAS_1', 'BF':'TEST_GAS_0'}},
        'TEST': {'Type': 'TypeBp', 'CELL':{ 'colum':1, 'line':1 }, 'BS':{ 'BF':'TEST_GAS_0', 'SF':'TEST_GAS_1'}}
    }

    height = 0
    width = 0
    contents = header
    before_cell_colum = 0
    before_cell_line = 0
    direct = 1 # 0: colum, 1:line
    with open('./OFFLOAD_OVERVIEW.adl','w') as f:
        for system in systems:
            type = model[system]['Type']
            bs = model[system]['BS']
            cell = model[system]['CELL']
            print type
            print bs

            if before_cell_colum > cell['colum']:
                height += h1+2
                width = 0
            elif before_cell_line > cell['line']:
                height = 0
                width += w1+2
            
            print width,height
            print cell['colum'],cell['line']

            if type == 'TypeA':
                txt,w1,h1 = usr_typea(x=width,y=height,system=system, **bs)
            elif type == 'TypeB':
                txt,w1,h1 = usr_typeb(x=width,y=height,system=system, **bs)
            elif type == 'TypeBp':
                txt,w1,h1 = usr_typebp(x=width,y=height,system=system, **bs)
            contents += txt            

            if direct == 0:
                height += h1+2
            else:
                width += w1+2

            before_cell_colum = cell['colum']
            before_cell_line = cell['line']

        f.write(contents)    
