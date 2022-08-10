#!/usr/bin/env python3

dnsfile = open("dnsservers.txt", "r")

dnslist = dnsfile.readlines()

for svr in dnslist: 

    print(svr, end="")

#best practice is to close your file
dnsfile.close()


