#!/usr/bin/env python
"""
	Program:	ssat_vocab.py

	Author:		C. McKnight

	Description:
		This program takes a JSON formatted data file and
		generates a GIFT formatted file for import into the
		Moodle 2 learning system. The contents of the GIFT
		file are determined by the desired type of quiz.

		Currently the program supports the following types
		of quizzes:

			Word Match 		  - A quiz that requires the student
								to select the definition that
								matches the word.

			Fill In The Blank - A quiz that requires the student
								to select the correct word to 
								complete the sentence.
"""

#####################################################################
# imports
#####################################################################
import json, argparse, sys
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
	parser = argparse.ArgumentParser(description='Generate GIFT format Moodle files.')
	parser.add_argument('-qt', '--quiztype', 
						help='Type of quiz: [ wordmatch | fillblank ] Default is wordmatch', 
						nargs='?', default='wordmatch')
	parser.add_argument('infile', metavar='filename', nargs='?')

	return vars(parser.parse_args())

#====================================================================

def load_file(filename):
	"""Unserializes JSON data into a dictionary

	Retrieves the serialized data structure into a dictionary.

	Args:
		filename - Name of the input file

	Returns:
		A dict mapping the data to its original structure. For example:

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
	if not (filename is None):
		try:
			with open(filename) as json_data:
				data = json.load(json_data)
				json_data.close()
		except:
			print("**Error**  Can't find " + filename + "!")
			exit()
	else:
		print("You must provide a valid file name!")
		exit()

	return data
#====================================================================
def main():
	# get the command line arguments
	myopts = parse_args()

	# import the data file
	databank = load_file(myopts['infile'])

	# call the requested quiz generator
	print "Generating " + myopts['quiztype']
	generate_quiz(databank, myopts['quiztype'])
	
#====================================================================

#####################################################################
# main program logic
#####################################################################

if __name__=='__main__':
	main()