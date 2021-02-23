#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" © Ihor Mirzov, 2021
Distributed under GNU General Public License v3.0

Shows the history of the keywords evolution
in Abaqus and Calculix """

import os
import re

# Clean screen
os.system('cls' if os.name=='nt' else 'clear')

# Get list of files to process
files = {}
for f in sorted(os.listdir('.')):
    match = re.findall(r'keywords_(.+)_(\d+)\.txt', f)
    if len(match):
        solver = match[0][0].upper()
        year = match[0][1]
        if solver in files:
            files[solver].append((year, f), )
        else:
            files[solver] = [(year, f), ]

# For each solver
for solver in files.keys():
    
    # If there are more then one file/year
    if len(files[solver]) < 2:
        continue

    # Get the first version to start comparison from
    year1, f1 = files[solver][0]
    print(solver, '- reference version is', year1)
    for i in range(len(files[solver]) - 1):
        year2, f2 = files[solver][i+1] # second version

        # Get all keywords in previous and current versions
        with open(f1, 'r') as f:
            lines1 = f.readlines()
        with open(f2, 'r') as f:
            lines2 = f.readlines()

        # Print comparison log
        print('\nNew keywords in', solver, year2)
        for line in lines2:
            if line not in lines1:
                print('\t', line.rstrip())

        year1, f1 = files[solver][i+1]