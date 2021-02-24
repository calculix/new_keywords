#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" © Ihor Mirzov, 2021
Distributed under GNU General Public License v3.0

Shows the history of the keywords evolution
in Abaqus and Calculix """

# TODO *WIND keywords is repeating in Abaqus

import os
import re

def main():

    # Clean screen
    os.system('cls' if os.name=='nt' else 'clear')

    # Get list of files to process
    files = {}
    for f in sorted(os.listdir('.')):
        match = re.findall(r'keywords_(.+)_(\d+)\.txt', f)
        if len(match):
            solver = match[0][0].upper()
            year = match[0][1]
            if 'CALCULIX' in solver:
                year = year[0] + '.' + year[1:]
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
        print('# ' + solver + '\n')
        print('The reference version is ' + year1 + '.\n')
        for i in range(len(files[solver]) - 1):
            year2, f2 = files[solver][i+1] # second version

            # Get all keywords in previous and current versions
            lines1 = []
            lines2 = []
            with open(f1, 'r') as f:
                 for l in f.readlines():
                     lines1.append(l.strip())
            with open(f2, 'r') as f:
                 for l in f.readlines():
                     lines2.append(l.strip())

            # Print comparison log
            print('New keywords in {} {}:\n'.format(solver, year2))
            count = 0
            for line in lines2:
                if line not in lines1:
                    print(' '*4 + line)
                    count += 1
            if not count:
                print(' '*4 + '-'*3)

            year1, f1 = files[solver][i+1]
            print()

if __name__ == '__main__':
    main()