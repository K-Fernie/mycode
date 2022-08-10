#!/usr/bin/env python3

import os
import zipfile

def zipdir(dirpath, zipfileobj):
    """does the work of writing data into our zipfile"""
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            print(os.path.join(root,file))
            zipfileobj.write(os.path.join(root, file))
    return None

def main():
    """called at runtime"""

    dirpath = input("What directory are we archiving today? ")

    if os.path.isdir(dirpath):
        zippedfin = input("What should we call the finished archive? ")

        with zipfile.ZipFile(zippedfin, "w", zipfile.ZIP_DEFLATED) as zipfileobj:

            zipdir(dirpath, zipfileobj)
    else:
        print("Run the script again when you have a valid directory to zip.")

main()
