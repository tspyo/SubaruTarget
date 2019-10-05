#! /usr/bin/env python 

# This script check the duplication of targets between the two target files.

import sys
import argparse
from os.path import basename

parser = argparse.ArgumentParser(description="Check the duplication of targets between the two target files",
                                 usage="{0} <in targetlist txt file> <ref targetlist txt file>".format(basename(__file__)))
                                 
if len (sys.argv[1:]) == 0:
	print()
	parser.print_help()
	print()
	parser.exit()
	
args = parser.parse_args()

in_file = sys.argv[1]
ref_file = sys.argv[2]

# check matching of 
