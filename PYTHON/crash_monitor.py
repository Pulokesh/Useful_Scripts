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
# Analysis of Ethylene trajectory; Average population vs. Time(fs)
#
######################################################################

import os
import sys
import math



def run():

    N = 40
    for i in range(0,N):

        f = open("run"+str(i)+"/x1.scf.out","r")
        A = f.readlines()
        f.close()
        LN = len(A)
        #print mx_sz
        complete = 1
        for j in xrange(LN):
            la = A[j].split()
            if len(la) >0 and la[0]=="stopping" and la[1]=="...":
                print "Crashed run_",i
                complete = 0
                break

        if complete ==1:
            print "run_",i," running smooth"

run()
