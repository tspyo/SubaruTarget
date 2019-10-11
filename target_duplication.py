#! /usr/bin/env python 

# This script check the duplication of targets between the two target files.

import sys
import argparse
from os.path import basename
from SubaruTarget import read_SubaruTargetList

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



in_targetlist = read_SubaruTargetList(in_file)
ref_targetlist = read_SubaruTargetList(ref_file)

# check matching of object_name
# check matching of ra and dec within 1 min (< 100.00)  hhmmss.ss and +/-ddmmss.ss   

for in_target in in_targetlist:
	for ref_target in ref_targetlist:
		duplicate_flag = False
		ra_diff = abs(in_target["ra"]-ref_target["ra"])
		dec_diff = abs(in_target["dec"]-ref_target["dec"])
		if in_target["ojbect_name"] == ref_target["object_name"]:
			duplicate_flag = True
		elif (ra_diff < 100.0) and (dec_diff < 100.0):
			duplicate_flag = True
			
		if duplicate_flag:
			print()  # blank line
			print(f"{in_target['object_name']} is duplicated with {ref_target['object_name']}.")
			print(in_target)
			print(ref_target)

