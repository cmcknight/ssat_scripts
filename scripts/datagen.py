#!/usr/bin/env python

"""
	Program: datagen.py

	Description:

	This program takes a tab-delimited file of words and definitions 
	and creates GIFT-formatted output files that are meant to be
	imported into the Moodle Learning Management System.

"""

####################################################################
# imports
####################################################################

import argparse, csv, sys

####################################################################
# methods
####################################################################

#===================================================================
# parse the command line argument(s)
#===================================================================
def parse_args():
	parser = argparse.ArgumentParser(description='Generate MOODLE GIFT-formatted Vocabulary Quizzes')
	parser.add_argument('infile', help="Usage: datagen.py filename lesson", metavar='filename')
	parser.add_argument('lesson', metavar='lesson')

	return vars(parser.parse_args())

#===================================================================
# load file
#===================================================================
def load_file(filename):
	mydict = {}

	if not (filename is None):
		for line in open(filename, 'r'):
			k,v = line.split("\t")
			#print("Key: " + k)
			#print("Value: " + v)
			mydict[k] = v.rstrip('\n')
	else:
		print("You must provide a file name.")
		exit()

	return mydict


#===================================================================
# gen_word_match
#===================================================================
def gen_word_match(data, keyset, header, filename):

	with open (filename, "w") as output:
		output.write(header)
		# iterate over the dictionary and write the entries to the output file
		for key in keyset:
			sentence = "The definition of word <b>%s</b> is: " % key
			output.write(sentence + "{\n")
			for answerkey in keyset:
				if answerkey == key:
					leader = "="
				else:
					leader = "~"
				output.write(leader + data[answerkey] + "\n")
			output.write("}\n\n")
	output.close
	

#===================================================================
# gen_fill_in_the_blanks
#===================================================================
def gen_fill_in_the_blank(data, keyset, header, filename):
	with open (filename, "w") as output:
		output.write(header)
		# iterate over the dictionary and write the entries to the output file
		for key in keyset:
			output.write('(' + data[key] + ") " + "{\n")
			for answerkey in keyset:
				if answerkey == key:
					leader = "="
				else:
					leader = "~"
				output.write(leader + answerkey + "\n")
			output.write("}.\n\n")
	output.close

#===================================================================
# gen_gift_data
#===================================================================
def gen_gift_data(data, lesson):
	
	sections = ('ACEGIKMOQSUWY', 'BDFHJLNPRTVXZ')
	
	# get the keys and sort them
	keys = data.keys()
	keys = sorted(keys)

	# determine how many sets of 10 are in the data
	datalen = len(data)
	num_sets = datalen / 10
	last_set = datalen - (num_sets * 10)
	if (last_set > 0):
		num_sets += num_sets

	# loop over the sets to generate the appropriate test files
	for loop in range(num_sets):

		# determine the starting and ending values for the keysets
		start_val = 0 + (loop * 10)
		end_val = last_set if (last_set > 0 and loop == num_sets - 1) else (loop * 10) + 9
		keyset = keys[start_val:end_val+1]

		filename = 'Lesson_' + str(lesson) + sections[0][loop] + '-Matching.txt'
		file_header = '$CATEGORY: SSAT Vocabulary/Vocabulary Builder/Lesson ' + \
					   str(lesson) + sections[0][loop] + '\n\n[html]\n'
		gen_word_match(data, keyset, file_header, filename)

		filename = 'Lesson_' + str(lesson) + sections[1][loop] + '-FillInTheBlank.txt'
		file_header = '$CATEGORY: SSAT Vocabulary/Vocabulary Builder/Lesson ' + \
					   str(lesson) + sections[1][loop] + '\n\n[html]\n'
		gen_fill_in_the_blank(data, keyset, file_header, filename)


#===================================================================
# main method
#===================================================================
def main():
	# get the command line arguments
	myopts = parse_args()

	# import the data file
	data = load_file(myopts['infile'])

	# generate GIFT data
	gen_gift_data(data, myopts['lesson'])

if __name__=='__main__':
	main()