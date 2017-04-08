#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Initialise – import and present
import sys, os, requests
from argparse import ArgumentParser
# os.system('clear') - optional, currently disabled
# Blank line seems to fix ASCII display error
print """
  ____                  _               _   _      
 / ___|  __ _ _ __   __| | ___ __ _ ___| |_| | ___ 
 \___ \ / _` | '_ \ / _` |/ __/ _` / __| __| |/ _ \

  ___) | (_| | | | | (_| | (_| (_| \__ \ |_| |  __/
 |____/ \__,_|_| |_|\__,_|\___\__,_|___/\__|_|\___|                                        
 
 S3 bucket enumeration // release v1.0.0 // ysx                       

"""
# Receive – target stem and argument check
targetStem = ""
parser = ArgumentParser()
parser.add_argument("-t", "--target", dest="targetStem",
                    help="Select a target stem name (e.g. 'instacart')", metavar="targetStem", required="True")
args = parser.parse_args()
with open('bucket-names.txt', 'r') as f: 
    bucketNames = [line.strip() for line in f] 
print "[*] Commencing analysis of target '%s', reading from '%s'." % (args.targetStem, f.name)
print ""
# Analyse – standard permutations and special exceptions
# TODO – alert to 403/200s or give readout at end?
for name in bucketNames:
	r = requests.head("http://%s%s.s3.amazonaws.com" % (args.targetStem, name))
	print("%s%s --> %s" % (args.targetStem, name, r.status_code))
# OPTIONAL – special exceptions, example hardcoded below
# print "[*] Now checking special exceptions."
# special1 = requests.head("http://assets.%s.com.s3.amazonaws.com" % args.targetStem)
# print("%s%s%s --> %s" % ("assets.", args.targetStem,".com", special1.status_code))
print("[+] Analysis complete. Please check for non-404 codes and anomalies.")
