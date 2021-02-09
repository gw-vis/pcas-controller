#!/usr/bin/env python3

header = '''
file {
	name="/opt/rtcds/userapps/release/cds/common/medm/phytron/OVERVIEW/PHYTRON_OVERVIEW.adl"
	version=030107
}
display {
	object {
		x=100
		y=56
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
'''

channel_dict = {
    'ETMX_PITCH_HR': 1,
    'ETMX_ROLL': 2,
    'ETMX_PITCH_AR': 3,
    
    'ITMX_PITCH_HR': 1,
    'ITMX_ROLL': 2,
    'ITMX_PITCH_AR': 3,

    'ETMY_PITCH_HR': 1,
    'ETMY_ROLL': 2,
    'ETMY_PITCH_AR': 3,

    'ITMY_PITCH_HR': 1,
    'ITMY_ROLL': 2,
    'ITMY_PITCH_AR': 3,

    'TEST_PITCH_HR': 1,
    'TEST_ROLL': 2,
    'TEST_PITCH_AR': 3,
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


def mini(x,y,system,phyid,motor,label,mode='ERR'):
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
    "composite file"="./OVERVIEW_MINI.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system},PHYID={phyid},MOTOR={motor},LABEL={label}"
    }}
    '''.format(common=common,x=x,y=y,system=system,phyid=phyid,label=label,motor=motor)
    return txt,width,height

def head(x,y,system):
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
    "composite file"="./HEAD_MINI.adl;IFO=$(IFO),ifo=$(ifo),SYSTEM={system}"
    }}
    '''.format(common=common,x=x,y=y,system=system)
    return txt,width,height

def foot(x,y):
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
    "composite file"="./FOOT_MINI.adl;IFO=$(IFO),ifo=$(ifo)"
    }}
    '''.format(common=common,x=x,y=y)
    return txt,width,height


def motor_is(system,dof):
    return channel_dict[system+'_'+dof]

def label_is(stage,dof):
    return dof
            
    
if __name__=='__main__':
#    systems = ['ETMX', 'ITMX', 'ETMY', 'ITMY', 'TEST']
    systems = ['ETMX', 'ITMX', 'ETMY', 'ITMY']

    dofs = {  'ETMX':['PITCH_HR','ROLL','PITCH_AR'],
              'ITMX':['PITCH_HR','ROLL','PITCH_AR'],
              'ETMY':['PITCH_HR','ROLL','PITCH_AR'],
              'ITMY':['PITCH_HR','ROLL','PITCH_AR'],
              'TEST':['PITCH_HR','ROLL','PITCH_AR']}

    mode = 'ERR'
    
    height = 10
    width = 0
    _h0 = height
    _w0 = width
    contents = header
    _h = 0
    _w = 0
    with open('./PHYTRON_OVERVIEW.adl','w') as f:
        txt,w0,h0 = top(width,height)
        contents += txt
        height += h0
        _h0 = height
        for num,system in enumerate(systems):
            print('{0}'.format(system))
            phyid = system                
            txt,w0,h0 = head(width,height,system)
            contents += txt         
            _h = h0
            for dof in dofs[system]:

                phyid = system
                motor = motor_is(system,dof)
                label = label_is(system,dof)
                    
                txt,w1,h1 = mini(width,height+_h,system,phyid,motor,label,mode=mode)
                _h += h1
                contents += txt

            txt,w2,h2 = foot(width,height+_h)
            contents += txt
            _h += h2
            _w = max(w0,w1,w2) + 2            
            q,mod = divmod(num+1,2)
            height = q*200 + _h0
            width = mod*_w + _w0
                
        f.write(contents)    
