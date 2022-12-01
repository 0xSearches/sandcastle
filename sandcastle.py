#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, subprocess, requests, platform
from argparse import ArgumentParser

print( """
   ____             __             __  __
  / __/__ ____  ___/ /______ ____ / /_/ /__
 _\ \/ _ `/ _ \/ _  / __/ _ `(_-</ __/ / -_)
/___/\_,_/_//_/\_,_/\__/\_,_/___/\__/_/\__/

S3 bucket enumeration // release v1.3.0 // SecurityShrimp

""")
targetStem = ""
inputFile = ""

parser = ArgumentParser()
parser.add_argument("-t", "--target", dest="targetStem",
                        help="Select a target stem name (e.g. 'shopify')", metavar="targetStem", required="True")
parser.add_argument("-f", "--file", dest="inputFile",
                        help="Select a bucket permutation file (default: bucket-names.txt)", default="bucket-names.txt", metavar="inputFile")
parser.add_argument("-a", "--awscli-path", dest="aws_path",
                        help = "Specify the file path for the location on disk of the AWS CLI binary",
                        metavar = "awspath",default=None)
args = parser.parse_args()

if platform.system() == "'Windows'":
        print("Sorry Windows is not currently a supported platform for Sandcastle")
else:
        with open(args.inputFile, 'r') as f:
                bucketNames = [line.strip() for line in f]
                lineCount = len(bucketNames)

        print(f"[*] Commencing enumeration of '{args.targetStem}', reading {lineCount} lines from '{f.name}'.")

        for name in bucketNames:
                r = requests.head(f"http://{args.targetStem}{name}.s3.amazonaws.com")
                if r.status_code != 404 and r.status_code != 400:
                        print (f"[+] Checking potential match: {args.targetStem}{name} -->  Bucket HTTP Response code:{r.status_code}")
                        if platform.system() == "'Darwin'":
                                check = subprocess.getoutput("/opt/homebrew/bin/aws s3 ls s3://{args.targetStem}{name}")
                                print(f"{check}")
                        elif platform.system() == "'Linux'":
                                check = subprocess.getoutput("/usr/local/bin/aws s3 ls s3://{args.targetStem}{name}")
                                print(f"{check}")
                        elif args.aws_path != None:
                                check = subprocess.getoutput("{args.aws_path} s3 ls s3://{args.targetStem}{name}")
                                print(f"{check}")
print (f"[*] Enumeration of '{args.targetStem}' buckets complete.")
