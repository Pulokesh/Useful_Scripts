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
# This script cancel a series of jobs from a list
#
######################################################################

import os
import sys
import math
import glob 

def cancel_jbs():
    FL=[]
    for i in xrange(20):
        os.chdir("/budgetdata/academic/alexeyak/ekadashi/NO_Au/NAMD/run%i"%i)
        for file in glob.glob("slurm*"):
            FL.append(file)
        #print(file)

    print FL
    for j in xrange(len(FL)):
        jid = FL[j].split(".")
        jbid = jid[0].split("-")[1]
        os.system("scancel -M chemistry %s"%jbid)

def run_jobs():
    for i in xrange(len(A)):
        #print A[i]
        os.system("scancel -M chemistry %s"%A[i])
        #os.system("scancel %i"%(float(A[i])))  # both of these works


#run_jobs()
cancel_jbs()
