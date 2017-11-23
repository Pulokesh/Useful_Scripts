#*********************************************************************************
#* Copyright (C) 2017 Ekadashi Pradhan
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
# Analysis of Quantum Yield of cis-trans isomerization
#
######################################################################

import sys
import os
import math

def srt_prod(ia):
    #fname = "run12/res/md_0_2_0.xyz_dihedral.txt"
    f=open("run%i/res/md_0_2_0.xyz_dihedral.txt"%ia,"r")
    A=f.readlines()
    f.close()
    N=len(A)
    cis,trans=0,0
    phi = float(A[N-1].split()[2])
    if phi<90.0:
        cis,trans=1,0
    else:
        cis,trans=0,1

    return cis,trans

##
# Main Function calling
ci,tra=[],[]
for i in xrange(30):
    cs,tr=srt_prod(i)
    if cs!=0:
        ci.append(i)
    if tr!=0:
        tra.append(i)
print "Cis= ",ci,"Trans= ",tra
cs_tot,tr_tot = len(ci),len(tra)
print "Cis total = ",cs_tot,"Trans total = ",tr_tot,"Yield% = ",(cs_tot/30.0)*100.0
#print "Cis= ",cs,"Trans= ",tr
