#!/usr/bin/env python3

header = '''
file {
	name="/opt/rtcds/userapps/release/vis/common/medm/steppingmotor/OVERVIEW/STANDALONE_STEPPER_OVERVIEW.adl"
	version=030107
}
display {
	object {
		x=1996
		y=56
		width=512
		height=400
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

channel_dict = {
    'TEST_P0_GAS': 0,
    'TEST_P1_GAS': 1,
    'TEST_P2_GAS': 2,
    'TEST_P3_GAS': 3,
    'TEST_P4_GAS': 4,
    'TEST_P5_GAS': 5
}


#common = '/opt/rtcds/userapps/release/vis/common'
common = './'

def top(x,y):
    width = 300
    height = 100
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


def mini(x,y,system,stage,dof,damp,bio,stepname,stepid,motor,label,mode='ERR'):
    width = 480
    height = 25
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=550
    height=30
    }}
    "composite name"=""
    "composite file"="./OVERVIEW_MINI.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},STAGE={stage},DOF={dof},DAMP={damp},BIO={bio},STEPNAME={stepname},STEPID={stepid},MOTOR={motor},LABEL={label}"
    }}
    '''.format(common=common,x=x,y=y,system=system,stage=stage,dof=dof,damp=damp,bio=bio,stepname=stepname,stepid=stepid,label=label,motor=motor)
    return txt,width,height

def head(x,y,system,mtype):
    width = 300
    height = 55
    txt = '''
    composite {{
    object {{
    x={x}
    y={y}
    width=300
    height=55
    }}
    "composite name"=""
    "composite file"="./HEAD_MINI.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},TYPE={mtype}"
    }}
    '''.format(common=common,x=x,y=y,system=system,mtype=mtype)
    return txt,width,height

def foot(x,y,stepperid):
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
    "composite file"="./FOOT_MINI.adl;IFO=$(IFO),ifo=$(ifo),STEPPERID={stepperid}"
    }}
    '''.format(common=common,x=x,y=y,stepperid=stepperid)
    return txt,width,height


def mtype_is(system):
    if 'TM' in system:
        mtype = 'TM'
    elif 'BS' == system:
        mtype = 'BS'
    elif 'SR' in system:
        mtype = 'SR'
    else:            
        mtype = None
    return mtype
    
def damp_is(system,mode='ERR'):
    if system in ['BS','SR2','SR3','SRM']:
        damp = 'DCCTRL'
    else:
        damp = 'DAMP'                        
    return damp
    
def bio_is(system):
    if system in ['BS','SR2','SR3','SRM']:
        bio = 'BIO'
    else:
        bio = 'BO'
    return bio
    
def stepname_is(dof):
    if dof == 'GAS':
        return 'STEP_GAS'
    else:
        return 'STEP_IP'

def stepperid_is(system):
    if system == 'PRM' or system == 'PR3':
        return 'PR0'
    else:
        return system

def stepid_is(system,stage):
    if stage == 'IP':
        return system+'_IP'
    else:
        return stepperid_is(system)+'_GAS'

def motor_is(system,stage,dof):
    if stage == 'IP':
        return dof
    else:
        return channel_dict[system+'_'+stage+'_'+dof]

def label_is(stage,dof):
    if stage == 'IP':
        if dof == 'F0Y':
            return 'F0_Y'
        if dof == 'A':
            return stage + '_H1'
        if dof == 'B':
            return stage + '_H2'
        if dof == 'C':
            return stage + '_H3'

    return stage + '_' + dof
            
    
if __name__=='__main__':
    systems = ['TEST'] # TEST

    # ERROR mode
    # TypeA
    #   K1:VIS-ITMY_IP_DAMP_L_INMON
    #   K1:VIS-ITMY_F0_DAMP_GAS_INMON
    # TypeB    
    #   K1:VIS-BS_IP_DCCTRL_L_INMON
    #   K1:VIS-BS_F0_DCCTRL_GAS_INMON
    # TypeBp
    #   K1:VIS-PR2_BF_DAMP_GAS_INMON
    #
    # FB mode 
    # TypeA
    #   K1:VIS-ETMY_IP_SUMOUT_L_OUTMON
    #   K1:VIS-ETMY_F0_SUMOUT_GAS_OUTMON
    # TypeB
    #   K1:VIS-BS_IP_DCCTRL_L_OUTMON
    #   K1:VIS-BS_F0_COILOUTF_GAS_OUTMON
    # TypeBp
    #   K1:VIS-PR2_SF_DAMP_GAS_OUTMON

    stages = {'TEST':['P0','P1','P2','P3','P4','P5']}

    dofs = {'P0':['GAS'],
            'P1':['GAS'],
            'P2':['GAS'],
            'P3':['GAS'],
            'P4':['GAS'],
            'P5':['GAS'],}
    mode = 'ERR'
    
    height = 10
    width = 0
    _h0 = height
    _w0 = width
    contents = header
    _h = 0
    _w = 0
    with open('./STANDALONE_STEPPER_OVERVIEW.adl','w') as f:
        txt,w0,h0 = top(width,height)
        contents += txt
        height += h0
        _h0 = height
        for num,system in enumerate(systems):
            print('{0}'.format(system))
            mtype = mtype_is(system)
            stepperid = stepperid_is(system)                
            txt,w0,h0 = head(width,height,system,mtype)
            contents += txt         
            _h = h0
            for stage in stages[system]:
                print(' - ',stage,dofs[stage])
                for dof in dofs[stage]:
                    damp = damp_is(system)
                    bio = bio_is(system)
                    stepname = stepname_is(dof)
                    stepid = stepid_is(system,stage)
                    motor = motor_is(system,stage,dof)
                    label = label_is(stage, dof)
                    
                    txt,w1,h1 = mini(width,height+_h,system,stage,dof,damp,bio,stepname,stepid,motor,label,mode=mode)
                    _h += h1
                    contents += txt
            txt,w2,h2 = foot(width,height+_h,stepperid)
            contents += txt
            _h += h2
            _w = max(w0,w1,w2) + 2            
            q,mod = divmod(num+1,4)
            height = q*320 + _h0
            width = mod*_w + _w0
                
        f.write(contents)    
