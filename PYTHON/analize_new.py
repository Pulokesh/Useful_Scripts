#*********************************************************************************
#* Copyright (C) 2017 Ekadashi Pradhan and Alexey V. Akimov
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
# Analysis of azobenzene trajectory
#
######################################################################

import os
import sys
import math
import copy

if sys.platform=="cygwin":
    from cyglibra_core import *
elif sys.platform=="linux" or sys.platform=="linux2":
    from liblibra_core import *
from libra_py import *

def angle_NNC(ra,rb):
    ##
    # Finds angle between two vectors
    # theta = cos^(-1) A(dot)B/|A||B|
    ab = ra.length()*rb.length()
    a_b = ra*rb
    theta_ab = math.degrees(math.acos(a_b/ab))

    return theta_ab
def angle(ri,rj,rk,rl):
    t = VECTOR()
    u = VECTOR()
    rp = VECTOR()

    direction = 1.0  # =1 - torsion;  =-1 - dihedral angle

    rij = ri - rj
    rkj = rk - rj
    rlk = rl - rk

    t.cross(rij, rkj)
    t = direction*t  

    u.cross(rlk, rkj)
    modt = t.length()
    modu = u.length()

    phi = 0.0

    if((modt!=0.0) and (modu!=0.0)):
        cos_phi = (t*u)/(modt*modu)
#        print "cos_phi= ",cos_phi
        if(cos_phi>= 1.0):
            cos_phi=1.0
        elif(cos_phi<=-1.0):
            cos_phi=-1.0

        rp.cross(t,u)
        sgn = 0.0
        if rkj*rp <0.0:
            sgn = -1.0
        else:
            sgn = 1.0

        phi = sgn*math.acos(cos_phi)

    return phi

def run(filename):

    #C3 - N12 - N13 - C14
    f = open(filename,"r")
    A = f.readlines()
    f.close()
    f1 = open("ene_0_2_0.txt","r")
    A1=f1.readlines()
    f1.close()

    sz = len(A)
    nsnaps = sz / (24 + 2)
    print "number of snaps = ", nsnaps
    r1 = VECTOR()
    r2 = VECTOR()
    r3 = VECTOR()
    r4 = VECTOR()

    f1 = open(filename+"_CNNC_NNC.txt","w")

    prev = 0.0
    cum = 0.0

    for t in xrange(nsnaps):
        s_C1 = A[t*26+(2+2)].split()
        s_N2 = A[t*26+(11+2)].split()
        s_N3 = A[t*26+(12+2)].split()
        s_C4 = A[t*26+(13+2)].split()
        ene_S2 = float(A1[t].split()[5])

        r1.x, r1.y, r1.z = float(s_C1[1]), float(s_C1[2]), float(s_C1[3])
        r2.x, r2.y, r2.z = float(s_N2[1]), float(s_N2[2]), float(s_N2[3])
        r3.x, r3.y, r3.z = float(s_N3[1]), float(s_N3[2]), float(s_N3[3])
        r4.x, r4.y, r4.z = float(s_C4[1]), float(s_C4[2]), float(s_C4[3])
    
        ang = angle(r1,r2,r3,r4)
        r21 = r2-r1
        r23 = r2-r3
        ang_NNC1 = angle_NNC(r21,r23)
        ang_NNC2 = angle_NNC(r3-r2,r3-r4)
#        print math.degrees(ang)
        d_ang = ang - prev   # change of angle during this step 

        d_ang_corr = d_ang

        if d_ang>math.pi:
            d_ang_corr = d_ang - 2.0*math.pi
        elif d_ang<-math.pi:
            d_ang_corr = d_ang + 2.0*math.pi

        cum = cum + d_ang_corr
        prev = ang
        
        #f1.write("%8.5f  %8.5f  %8.5f %10.5f %10.5f \n" % ( t, cum, math.degrees(math.fabs(ang)),ang_NNC1,ang_NNC2 ) )
        f1.write("%8.5f  %8.5f  %8.5f %10.5f %10.5f %10.6f \n" % ( t, cum, math.degrees(math.fabs(ang)),ang_NNC1,ang_NNC2,ene_S2 ) )
    f1.close()
    
run("md_0_2_0.xyz")
#run("tsh_copy_1.xyz")

