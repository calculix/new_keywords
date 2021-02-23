#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" © Ihor Mirzov, 2021
Distributed under GNU General Public License v3.0

Removes Abaqus and Calculix keyword duplicates """


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