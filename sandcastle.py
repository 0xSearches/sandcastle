#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Initialise – import and present
import sys, os, requests
from argparse import ArgumentParser
print """
  ____                  _               _   _      
 / ___|  __ _ _ __   __| | ___ __ _ ___| |_| | ___ 
 \___ \ / _` | '_ \ / _` |/ __/ _` / __| __| |/ _ \

  ___) | (_| | | | | (_| | (_| (_| \__ \ |_| |  __/
 |____/ \__,_|_| |_|\__,_|\___\__,_|___/\__|_|\___|                                        
 
 S3 bucket enumeration // release v1.1.0 // ysx                       

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
print " "
# Analyse – standard permutations and special exceptions
for name in bucketNames:
	r = requests.head("http://%s%s.s3.amazonaws.com" % (args.targetStem, name))
	if r.status_code != 404:
		print "[+] Match: %s%s --> %s" % (args.targetStem, name, r.status_code)
	else:
		sys.stdout.write('')
		# Non-matching analysis disabled by default
		# print "[-] No match: %s%s --> %s" % (args.targetStem, name, r.status_code)
print "[+] Analysis of '%s' complete." % (args.targetStem)
