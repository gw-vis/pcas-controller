#!/bin/bash

version="3"
miyopico="/opt/rtcds/userapps/release/cds/common/medm/picomotor/miyopico"
pico="/opt/rtcds/userapps/release/cds/common/medm/picomotor"

# 0. make prottype medm file

# 1. Generate each driver medm file.
#rm ../*.adl
driver_name=("MCI" "MCO" "MCE" "STM1" "STM2" "IMMT1" "IMMT2" "POM1" "PR2" "PR3" "BS" "EX" "EY")
for driver in ${driver_name[@]};do
    cp ${miyopico}/MIYOPICO_VER${version}_PIT.adl ${pico}/PICO-${driver}_IM_PIT.adl
    sed -e 's/PIT/YAW/g' ${pico}/PICO-${driver}_IM_PIT.adl > ${pico}/PICO-${driver}_IM_YAW.adl 
done

# 2. Remove *.adl
# rm ../*.adl
