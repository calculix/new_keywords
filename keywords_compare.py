#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""© Ihor Mirzov, 2021-2024
Distributed under GNU General Public License v3.0

Shows the history of the keywords evolution
in Abaqus and Calculix.
"""

import os
import re


def filtr1():
    """Removes keyword duplicates in a file."""

    # file_name = 'keywords_abaqus_2020.txt'
    file_name = 'keywords_calculix_215.txt'

    with open(file_name, 'r') as f:
        lines = f.readlines()

    print('Before filter:', len(lines))
    lines = sorted(set(lines))
    print('After filter:', len(lines))

    for l in lines:
        print(l.strip())

    # with open(file_name, 'w') as f:
    #     f.writelines(lines)
    pass


def filtr2():
    """Find all uppercase lines in a file."""

    file_name = 'keywords_abaqus_2024.txt'
    keywords = []
    with open(file_name, 'r') as f:
        for l in f.readlines():
            if l and l == l.upper():
                keywords.append('*' + l.lstrip())
    keywords = sorted(set(keywords))
    for l in keywords:
        print(l.strip())
    print(len(keywords))
    # with open(file_name, 'w') as f:
    #     f.writelines(keywords)
    pass


def compare():
    """Perform comparison and write report."""

    # Get list of files to process
    files = {}
    d = '.'
    for f in sorted(os.listdir(d)):
        match = re.findall(r'keywords_(.+)_(\d+)\.txt', f)
        f = os.path.normpath(os.path.join(d, f))
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

    # Clean screen
    os.system('cls' if os.name=='nt' else 'clear')

    # filtr1()
    # filtr2()
    compare()
