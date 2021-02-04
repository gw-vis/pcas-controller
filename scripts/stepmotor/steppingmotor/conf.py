channel = {
        "PR2_GAS":{
                "config"  : 'PR2',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "PR0_GAS":{
                "config"  : 'PR0',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "ITMX_GAS":{
                "config"  : 'ITMX',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "ETMX_GAS":{
                "config"  : 'ETMX',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "ITMY_GAS":{
                "config"  : 'ITMY',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "ETMY_GAS":{
                "config"  : 'ETMY',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "BS_GAS":{
                "config"  : 'BS',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "SR2_GAS":{
                "config"  : 'SR2',
#                "axisDirection" : [ -1, -1, 1, 1, 1, 1 ]  # 0:BF:Negative, 1:F1:Negative, 2:F0:Positive. by KLog#15272
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "SR3_GAS":{
                "config"  : 'SR3',
#                "axisDirection" : [ -1, 1, 1, 1, 1, 1 ]   # 0:BF:Negative, 1:F1:Fishing rod not functional, 2:F0:Positive. by KLog#15272
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "SRM_GAS":{
                "config"  : 'SRM',
#                "axisDirection" : [ -1, -1, 1, -1, 1, 1 ] # 0:BF:Negative, 1:F1:Negative, 3:F0:Negative. by KLog#15272
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "BS_IP":{
                "config"  : 'BS',
                "motorA"  : 0,
                "motorB"  : 1,
                "motorC"  : 2,
                "motorY"  : 3,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1,
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "SR2_IP":{
                "config"  : 'SR',
                "motorA"  : 0,
                "motorB"  : 1,
                "motorC"  : 2,
                "motorY"  : 3,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1,  # L:Positive(Foward), T:Positive(Left), Y:Positive(CCW). by KLog#15272 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "SR3_IP":{
                "config"  : 'SR',
                "motorA"  : 0,
                "motorB"  : 4,
                "motorC"  : 2,
                "motorY"  : 3,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, # L:Positive(Foward), T:Positive(Left), Y:Positive(CCW). by KLog#15272 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "SRM_IP":{
                "config"  : 'SR',
                "motorA"  : 0,
                "motorB"  : 1,
                "motorC"  : 2,
                "motorY"  : 5,          # 4 -> 5
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, # L:Positive(Foward), T:Positive(Left), Y:Positive(CCW). by KLog#15272 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "ETMY_IP":{
                "config"  : 'TM',
                "motorA"  : 1,
                "motorB"  : 2,
                "motorC"  : 3,
                "motorY"  : 0,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "ETMX_IP":{
                "config"  : 'TM',
                "motorA"  : 1,
                "motorB"  : 2,
                "motorC"  : 3,
                "motorY"  : 0,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "ITMY_IP":{
                "config"  : 'TM',
                "motorA"  : 1,
                "motorB"  : 2,
                "motorC"  : 3,
                "motorY"  : 0,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "ITMX_IP":{
                "config"  : 'TM',
                "motorA"  : 1,
                "motorB"  : 2,
                "motorC"  : 3,
                "motorY"  : 0,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        # for TEST.
        # for Testing.
        "TEST_GAS":{
                "config"  : 'TEST',
                "axisDirection" : [ 1, 1, 1, 1, 1, 1 ]
                },
        "TESTBS_IP":{
                "config"  : 'BS',
                "motorA"  : 0,
                "motorB"  : 1,
                "motorC"  : 2,
                "motorY"  : 3,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "TESTSR_IP":{
                "config"  : 'SR',
                "motorA"  : 0,
                "motorB"  : 1,
                "motorC"  : 2,
                "motorY"  : 3,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                },
        "TESTTM_IP":{
                "config"  : 'TM',
                "motorA"  : 1,
                "motorB"  : 2,
                "motorC"  : 3,
                "motorY"  : 0,
                "signA"    : 1,
                "signB"    : 1,
                "signC"    : 1,
                "signY"    : 1,
                "axisDirectionLEN"  : 1, 
                "axisDirectionTRA"  : 1,
                "axisDirectionYAW"  : 1,
                "axisDirectionF0Y"  : 1,
                "axisDirectionA"  : 1, 
                "axisDirectionB"  : 1,
                "axisDirectionC"  : 1
                }
}
      

NAME = {\
    "PR3":"10.68.10.250",
}
