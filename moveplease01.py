#!/usr/bin/env python3

import shutil
import os

def main():
    #setting the current directory for the application
    os.chdir('/home/student/mycode/')

    #moving the object to storage
    shutil.move('raynor.obj', 'ceph_storage/')
    
    #renaming the second object that will be moved to storage
    xname = input('What is the new name for kerrigan.obj? ')

    #performs the same action as using mv to rename a file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
