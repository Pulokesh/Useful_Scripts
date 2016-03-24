#! /usr/bin/env python
import os
import math
from  numpy import *

##
# This python script generates gnuplot script which fits initial excitation energies (A_i)
# with relaxation time (tau_i)
# The exponential decay function to which the curve is fitted, is E(t) = E*exp(t/tau)
filename = "sh_en_ex"
no_ex = 31
fout = open("plt_gen", 'w')
# opens se_en and sh_en files and read initial excitation energies
for i in range(no_ex):
#    f = open("sh_en_ex%i" %i,'r') 
    f = open(filename+str(i),'r') 
    f_read = f.readlines()
    for j in range(len(f_read)):
        s = f_read[j].split()
        if j == 0 :
            A = float(s[3])
            break
    # Writing initial excitation energies
    fout.write("A"+str(i)+" = "+str(A)+'\n')
for i in range(no_ex):
    fout.write("f"+str(i)+"(x) = A"+str(i)+"*exp(-x/tau"+str(i)+")"+'\n')
    fout.write("tau"+str(i)+" = 20"+'\n')
#    fout.write("fit f"+str(i)+"(x) \"sh_en_ex"+str(i)+"\" u 2:4 via A"+str(i)+", tau"+str(i)+'\n')
    fout.write("fit f"+str(i)+"(x) \""+filename+str(i)+"\" u 2:4 via A"+str(i)+", tau"+str(i)+'\n')

fout.write("set print \"tmp.dat\""+'\n')

for i in range(no_ex):
    fout.write("print A"+str(i)+",tau"+str(i)+'\n')
fout.close()
