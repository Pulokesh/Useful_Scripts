#*********************************************************************************
#* Copyright (C) 2017 Ekadashi Pradhan
#*
#* This file is distributed under the terms of the GNU General Public License
#* as published by the Free Software Foundation, either version 2 of
#* the License, or (at your option) any later version.
#* See the file LICENSE in the root directory of this distribution
#* or <http://www.gnu.org/licenses/>.
#*


import os
import sys
import math

import time

path_org = os.getcwd()


#for i in xrange(100):
###################################
#      Creating folders
###################################
##
def clone_folder():
    for i in range(1,100):
        os.system("cp -r run0 run%i"%i)
###################################

###################################
#       Submiting jobs
###################################
#for i in xrange(5):

def time_gap(a):
    
    status = 0
    while status != 1:
        b=0
        b=int(time.time())
        print b
        print b-a
        if (b-a)%120 ==0:
            status = 1
    return status

def run_jobs(ia,ib):
    #for i in range(0,5):
    #    status = 0
    #    a = int(time.time())
    #    status = time_gap(a)
    #    print "status",status
    #    if status == 1:   # 1 = yes run, 0 = no don't, wait for the proper interval
    #        print "RUN %i at %i "%(i,int(a))
    for i in xrange(ib):
        os.chdir("run%i"%(ia*ib+i))
        #os.system("cp ../submit_templ_qe.slm ./")
        #os.system("cp ../run_qe.py ./")
        os.system("sbatch submit_templ_qe.slm")
    
        os.chdir(path_org)
###################################
    #os.system("rm -rf run%i"%i)
#os.system("cp x0.exp.in wd")
#os.system("cp x1.exp.in wd")
#os.chdir("wd")
######Run Calculation ###########
#clone_folder()
#a = int(time.time())
#while status != 0:

def delay_jobs():
    a0 = int(time.time())
    T = 3600 # Delay time 1 hr = 3600 sec
    ni = 10 # ni # of jobs at a time
    N = 10  # N*ni = 100 total jobs

    #run_jobs(0,ni)  # Runs first 5 jobs immediately
    run_jobs(2,10)  # Runs first 5 jobs immediately
    for i in range(3,N):  # Total
    #for i in range(1,N):  # Total
        a=int(time.time())

        while (a - a0)/T != 1 :  # This means 3 hours interval 5 jpbs will be submitted
            a=int(time.time())
        print "Current time = ",int(time.time())," JOB RUN = ",i*ni," to ",i*ni+ni-1
        run_jobs(i,ni)
        a0 = a

#clone_folder()
delay_jobs()    
#run_jobs()
print "Done"

