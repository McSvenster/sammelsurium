#!/bin/env python
###
# Skript um Daten aus Aleph sequential in csv zu schreiben
# ETH Library: Sven Koesling
# Oktober 2018
import sys
import re

inputfile = sys.argv[1]

fields = {"245": "$$a", "100": "$$a", "260": "$$c", "PST": "$$j"}

outputfile = open("ausgabe.csv", "w")

rec = { "100": "Autor", "245": "Titel", "260": "Publikationsdatum", "PST": "Signatur", "sysno": "Systemnummer"}

with open(inputfile, 'r') as sequa:
    for line in sequa:
        '''zeilenweises Abarbeiten des sequential-files'''
        if (line[:9] != rec["sysno"]):
            # print("Record", rec["sysno"], "wird in csv geschrieben.")
            output = "\";\"".join([rec["100"], rec["245"], rec["260"], rec["PST"], rec["sysno"]])
            outputfile.write("\"" + output + "\"\n")
            rec = {"100": "", "245": "", "260": "", "PST": "", "sysno": line[:9]}

        if (line[10:13] in fields.keys() and fields[line[10:13]] in line):
            try:
                content = re.search(re.escape(fields[line[10:13]]) + '(.+?)\$\$', line).group(1)
            except AttributeError:
                content = re.search(re.escape(fields[line[10:13]]) + '(.+?)$', line).group(1)
            rec[line[10:13]] = content

outputfile.close
