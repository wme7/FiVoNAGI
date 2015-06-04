#!/usr/bin/python
#

import numpy 
from scipy import interpolate, stats
import os
import sys
import glob
import re

# The idea of this "special 2" was to be able to restrict etaValues to
# 5,10,20, and pValues to 2. etaValues was finally not restricted.

angleValues = ["00000", "PIo32", "PIo16", "PIo08", "PIo04"]
etaValues = [5, 10, 20, 41, 82]
cflValues = [60, 70, 80, 90, 99]
pValues = [2]

resultsPath = str(sys.argv[1])
deployPath = str(sys.argv[2])

p_e_path = deployPath + '/dr_error_etas_CPU_special_2'
if not os.path.isdir(p_e_path) :

    os.mkdir(p_e_path)
    os.chdir(p_e_path)

    for angleIndex, angleV in enumerate(angleValues) :
        for cflIndex, cflV in enumerate(cflValues) :
            for pIndex, pV in enumerate(pValues) :
                
                outfile_name = 'error-cfl{0}-p{1}-angle{2}.dat'.format(cflV,pV,angleV)
                outfile = open(outfile_name,'w')
                outfile.write("# eta frame T error_L1 error_L2 error_Li\n")

                for etaIndex, etaV in enumerate(etaValues) :

                    execName = 'eta{0}-cfl{1}-p{2}-angle{3}'.format(etaV,cflV,pV,angleV)
                    refPath = deployPath + "/dr_error_etas_CPU/d-" + \
                              execName + "/u1-error.dat"

                    fm = open(refPath,'r')
                    line = 1
                    while line :
                        last_line = line                        
                        line = fm.readline()
                    fm.close()

                    outfile.write(str(etaV) + " " + last_line)
                outfile.close()
