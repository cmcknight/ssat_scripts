#!/usr/bin/env python
"""
	Program:	gen_json.py

	Author:		C. McKnight

	Description:
		This program takes a tab-delimited data file and
		generates a JSON formatted file for use by the 
		GIFT Vocabulary Quiz generators.

		Output format:

		{
			'Moodle GIFT Header' : {
				'course' : 'SSAT Vocabulary',
				'category' : 'Vocabulary Builder',
				'lesson' : 'Lesson 5A' },
			'wordbank' : {
		 		'brash' : {
		 			'definition' : "bold; hasty or lacking in sensitivity',
		 			'sentence' : 'The commander made a (bold) {} maneuver to \
		 			keep his opponent off balance.'
		 		},
		 		'benevolent' : {
		 			'definition' : "kind, good, caring',
		 			'sentence' : 'Although everyone originally though the new \
		 			 teacher was too strict, they began to see him as more of \
		 			 a (caring) {} person over time.'
		 		}
			}
		}

	Note:
		The curly braces embedded in the 'sentence' value are used to 
		mark the point where the list of words should appear.

"""

#####################################################################
# imports
#####################################################################
import json, argparse, sys, os
from giftgens import *
from pprint import pprint

#####################################################################
# methods
#####################################################################

#====================================================================

def parse_args():
	"""Parse the command line arguments

	Args:
		None

	Returns:
		Name of the data file to be loaded.
	"""
	parser = argparse.ArgumentParser(description='Generate JSON format files for GIFT quiz.')
	parser.add_argument('infile', metavar='filename', nargs='?')

	return vars(parser.parse_args())

#====================================================================

def convert_file(inp_file, out_file):
	if not (inp_file is None):
		try:
			with open(filename)

#====================================================================
def main():
	# get the command line arguments
	myopts = parse_args()

	# create the new filename
	tmpfile = os.path.splitext(myopts['infile'])[0] + ".json"

	# import the data file
	data = load_file(myopts['infile'])

	# call the requested quiz generator
	print "Generating " + tmpfile
	#generate_quiz(data)
	
#====================================================================

#####################################################################
# main program logic
#####################################################################

if __name__=='__main__':
	main()