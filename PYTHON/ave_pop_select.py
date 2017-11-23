#*********************************************************************************
#* Copyright (C) 2017 Ekadashi Pradhan, Alexey V. Akimov
#*
#* This file is distributed under the terms of the GNU General Public License
#* as published by the Free Software Foundation, either version 2 of
#* the License, or (at your option) any later version.
#* See the file LICENSE in the root directory of this distribution
#* or <http://www.gnu.org/licenses/>.
#*
#*********************************************************************************/

######################################################################
#
# Analysis of TSH population; Average population vs. Time(fs)
#
######################################################################

import os
import sys
import math

def run():
    ##
    dt = 1.0 / 41.34145  # 41.34145 = 1 fs
    sz,NR,nr1 = [],[],[]
    for i in xrange(40):
        f = open("run%i/res/sh_pop_ex2.txt"%i,"r")
        A = f.readlines()
        f.close()
        la = len(A)
        nr1.append(la)
        if A[la-1].split()[4]=="0.00000":  # For those completely relaxed trajectories
            NR.append(i)
            sz.append(len(A))  # how many lines
    N =len(NR)
    print "Traj lengths= ",nr1
    print "Relaxed trajectories number = ", len(NR), "Trajectories= ",NR
    mn_sz,mx_sz = min(sz),max(sz)
    print "Number of lines = ", mn_sz,sz.index(mn_sz), mx_sz
    print sz
    mx_run = NR[sz.index(mx_sz)] #+ 100

    f = open("run%i/res/sh_pop_ex2.txt"%mx_run,"r")
    A = f.readlines()
    f.close()

    T = []
    P = []
    for a in A:
        tmp = a.split()
        T.append( float(tmp[1]) * dt )
        P.append( 0.0 )
    for i in NR:
        f = open("run"+str(i)+"/res/sh_pop_ex2.txt","r")
        A = f.readlines()
        f.close()
        la = len(A)
        if la < mx_sz: # If particular trajectory is not completed
            for j in xrange(mx_sz-la):
                #A.append("1.00 1.00 1.00 1.00 Added lines")
                A.append(A[la-1]) # Keep the last population till end
        for n in xrange(mx_sz):
            tmp = A[n].split()
            P[n] = P[n] + (1.0/N) * float(tmp[2]) 
            # If the result is not completed for this trajectory, then dont
            # take it in to account
           #P[n] = P[n] 


    f1 = open("relax_total0.txt","w")
    for n in xrange(mx_sz):
        f1.write("%8.5f  %8.5f\n" % ( T[n], P[n]) )
    f1.close()

run()
