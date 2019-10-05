#! /usr/bin/env python

def read_SubaruTargetList(filename):

# Target list format: CSV :  object_name, RA, DEC, Epoch
	column_names = ['object_name', 'ra', 'dec', 'epoch']
	targetlist = []
	with open(filename) as targetfile:
		for line in targetfile:
			if line[0] == '#':
				continue # comment, go to next line
			else:
				line = line.rstrip("\n") # remove trailing new line
				target_info= dict(zip(column_names, line.split(",")))
				targetlist.append(target_info)
	assert(len(targetlist) >0, "Target list wasn't read!")		
				
	return targetlist
	
