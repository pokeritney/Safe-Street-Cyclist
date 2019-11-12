#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:52:55 2019

@author: tingli
"""

import os
import csv

with open('names.csv') as f:
    lines = csv.reader(f)
    for line in lines:
        try:
            os.rename(line[0],line[1] )
        except:
            print(line[0],line[1])
