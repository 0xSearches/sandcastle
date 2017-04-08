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
 S3 bucket enumeration // public release v0.1 // ysx                       
"""
# Receive – target stem and argument check
webStem = ""
parser = ArgumentParser()
parser.add_argument("-t", "--target", dest="webStem",
                    help="Select a target stem name (e.g. 'instacart')", metavar="webStem", required="True")
args = parser.parse_args()
with open('bucket-names.txt', 'r') as f: 
    bucketNames = [line.strip() for line in f] 
print "[*] Commencing analysis of target '%s', reading from '%s'." % (args.webStem, f.name)
print ""
# Analyse – standard permutations and special exceptions
for name in bucketNames:
	r = requests.head("http://%s%s.s3.amazonaws.com" % (args.webStem, name))
	print("%s%s --> %s" % (args.webStem, name, r.status_code))
# Optional – special exceptions, example hardcoded below
print "[*] Now checking special exceptions."
special1 = requests.head("http://assets.%s.com.s3.amazonaws.com" % args.webStem)
print(args.webStem, "assets", special1.status_code)
print("[+] Analysis complete. Please check for non-404 codes and anomalies.")