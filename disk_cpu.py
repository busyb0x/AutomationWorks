# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:37:11 2020
File Name: disk_cpu.py

This is a script to check disk and cpu usage.

@author: BusyB0x
"""
#!/usr/bin/env python3

import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    pf = (du.free/du.total)*100
    return pf > 50.0

def check_cpu_usage(seconds):
    cu = psutil.cpu_percent(seconds)
    return cu < 70.0

if not check_disk_usage("/") or not check_cpu_usage(60):
    print("CHECK THE PERFORMANCE")
else:
    print("USAGE IN SAFE LEVELS")
