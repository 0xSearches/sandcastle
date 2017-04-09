#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Initialise – import and present
import sys, os, requests
from argparse import ArgumentParser
print """
   ____             __             __  __   
  / __/__ ____  ___/ /______ ____ / /_/ /__ 
 _\ \/ _ `/ _ \/ _  / __/ _ `(_-</ __/ / -_)
/___/\_,_/_//_/\_,_/\__/\_,_/___/\__/_/\__/ 
                                            
S3 bucket enumeration // release v1.2.0 // ysx
"""
# Receive – target stem and argument check
targetStem = ""
inputFile = ""
parser = ArgumentParser()
parser.add_argument("-t", "--target", dest="targetStem",
                    help="Select a target stem name (e.g. 'instacart')", metavar="targetStem", required="True")
parser.add_argument("-f", "--file", dest="inputFile",
                    help="Optional: select a bucket permutation file (default: bucket-names.txt)", default="bucket-names.txt", metavar="inputFile")
args = parser.parse_args()
with open(args.inputFile, 'r') as f: 
    bucketNames = [line.strip() for line in f] 
    lineCount = len(bucketNames)
print "[*] Commencing enumeration of target '%s', reading %i lines from '%s'." % (args.targetStem, lineCount, f.name)
# Enumerate – standard permutations and status code analysis
for name in bucketNames:
	r = requests.head("http://%s%s.s3.amazonaws.com" % (args.targetStem, name))
	if r.status_code != 404:
		print "[+] Match: %s%s --> %s" % (args.targetStem, name, r.status_code)
	else:
		sys.stdout.write('')
		# Non-matching analysis disabled by default
		# print "[-] No match: %s%s --> %s" % (args.targetStem, name, r.status_code)
print "[+] Enumeration of '%s' complete." % (args.targetStem)
