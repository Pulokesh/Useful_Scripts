#*****************************************************
#* Copyright (C) 2017 Ekadashi Pradhan
#*****************************************************

##
# This code will sort CNNC from the CNNC_NNCC energy data
# and write like NNCC_CNNC. It is useful for analyze a particular cut
# of one coordinate while other is fixed, when you have 2D cuts.
#
#   Example input         output
#   R1 R2 V(R1,R2)      R1 R2 V(R1,R2)
#   0 0 0.0             0 0 0.0
#   0 1 0.2             1 0 0.1
#   0 2 0.5             2 0 0.2

#   1 0 0.1             0 1 0.2
#   1 1 0.3      to     1 1 0.3
#   1 2 0.4    ------\  2 1 0.6
#              ------/
#   2 0 0.2             0 2 0.5
#   2 1 0.6             1 2 0.4
#   2 2 0.8             2 2 0.8


import math
import os
import sys

def sort():
    fin = open("coord_switch.in","r")
    A=fin.readlines()
    fin.close()
    N1 = 31
    N2 = 32
    N = len(A)
    fut = open("coord_switch.out","w")
    for i in xrange(N2-1):
        for j in xrange(N1):
            fut.write("%s"%A[j*N2+i])
        fut.write("\n")
    fut.close()
 
sort()
