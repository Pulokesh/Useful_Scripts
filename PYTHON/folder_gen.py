#*****************************************************
#* Copyright (C) 2017 Ekadashi Pradhan
#*****************************************************
import os
import sys
import math

import time

path_org = os.getcwd()


###################################
#      Creating folders
###################################
##
def clone_folder():
##
# First create run0 folder with every necessary files in it
# Then just copy run0 to many folders with increasing indexes
    for i in range(1,10):
        os.system("cp -r run0 run%i"%i)
###################################

def check_job_status(i,ni):
    f = open("run%i/x0.scf.out"%(i*ni-1),"r")
    A = f.readlines()
    f.close()
    status = 0
    for s in A:
        sa = s.split()
        # Line says "convergence has been achieved in -- iterations"
        if len(sa)>0 and sa[0]=="convergence" and sa[1]=="has" and sa[3]=="achieved":
            status = 1 # job completed 
        
    return status

def run_jobs(ia,ib):
    for i in xrange(ib):
        os.chdir("run%i"%(ia*ib+i))
        #os.system("cp ../submit_templ_qe.slm ./")
        #os.system("cp ../run_qe.py ./")
        os.system("sbatch submit_templ_qe.slm")
    
        os.chdir(path_org)
###################################

def control_jobs_queue():
    t0 = int(time.time())
    T = 10 # Check convergence in everg 10 sec 
    ni = 1 # ni # of jobs at a time
    N = 10  # N*ni = 10 total jobs

    run_jobs(0,1)  # Runs first job immediately
    for i in range(1,N):  # Running remaining jobs one at a time
        t1=int(time.time())
        status = 0
        while status !=1: # Until previous job is finished
            while (t1 - t0)/T != 1 :  # This means 10 sec interval
                t1=int(time.time())
            print "Current time = ",int(time.time())," JOB RUN = ",i*ni," to ",i*ni+ni-1
            status = check_job_status(i,ni) #  status = 1 if the last job is completed, else 0
            t0 = t1
        run_jobs(i,ni)
        t0 = t1

#clone_folder()
control_jobs_queue()    
#run_jobs()
print "Done"

