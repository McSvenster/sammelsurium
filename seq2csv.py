#!/bin/env python
###
# Skript um Daten aus Aleph sequential in csv zu schreiben
# ETH Library: Sven Koesling
# Oktober 2018
import sys

inputfile = sys.argv[1]

fields = {"245": "$$a", "100": "$$a", "264": "$$c", "PST4": "$$j"}

sysno = ""
with open(inputfile, 'r') as sequa:
    for line in sequa:
        '''zeilenweises Abarbeiten des sequential-files'''
        if (line[:9] != sysno):
            # print("Record", sysno, "wird in csv geschrieben.")
            sysno = line[:9]
            rec = {}

        if (line[10:13] in fields.keys() and fields[line[10:13]] in line):
            rec[line[10:13]] = "bla"
            print(line)
