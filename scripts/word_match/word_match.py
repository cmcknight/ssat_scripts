#################################################################
# Program:		word_match.py
# Version:		1.0
# Description:
#	This program creates a GIFT import formatted text file for a
# match the word Moodle quiz.
#
# Inputs:
# 	The program expects a text file with a $CATEGORY header as 
# its first line followed by a set of delimited lines of words 
# and their definitions.
#
# Command Line Switches:
#	-d 		Delimiter string (TAB by default)
#	-h 		Help
#	-f 		Name of input file (stdin by default)
#################################################################

#################################################################
# Imports Section
#################################################################
import argparse, sys


#################################################################
# Method:		parse_args()
#
# Description:	Parse the command line arguments into a dictionary
#
# Arguments:	None
#
# Returns:		A dictionary containing the command line
# 				arguments
#################################################################
def parse_args():
	# create an instance of an argparse object
	parser = \
		argparse.ArgumentParser(description='Process text files for word match GIFT output.')

	####################################
	# add the arguments for the parser #
	####################################

	# -d for the delimiter, default value of the tab character
	parser.add_argument('-d', metavar='delimiter', nargs='?', 	
		default="\t")

	# open an input stream based on the filename provided in infile
	# otherwise, default to the standard input stream
	parser.add_argument('-f', metavar='filename', nargs='?', default="-")

	# parse the command line arguments
	ns = parser.parse_args()

	return vars(ns)


#################################################################
# Method:		load_file(args)
#
# Description:	Load the file contents
#
# Arguments:	args - a list of command line arguments
#
# Returns:		lines - a list of strings containing the file
#						contents
#################################################################
def load_file(args):
	# default the input file to the system standard input stream
	input_file = sys.stdin

	# assign to associated variables
	filename = args['f']
	delimiter = args['d']

	# open the input stream
	if (filename != '-'):
		try:
			input_file = open(filename, 'r')
		except IOError:
			print("\n******************* Error ********************\n")
			print("I'm sorry, the file [" + filename + "] does not exist.")
			print("\n******************* Error ********************\n")
			exit()

	# load the file into a list
	lines = input_file.readlines()

	# close the file
	input_file.close()

	return lines


#################################################################
# Method:		process_data(data)
#
# Description:	Process the file contents
#
# Arguments:	data - a list of strings containing the file 
#					   contents
#
# Returns:		A list containing a word/def list, a filename,
#				and a category for the lesson
#################################################################
def process_data(data):
	words_and_defs = list()

	# loop over the file contents
	lesson_category = ""
	for line in data:
		line = line.strip("\r\n")
		# capture the course/lesson/category info
		if (line.startswith("$CATEGORY")):
			# keep category line intact
			lesson_category = line
		else:
			# get the word and definition
			line = line.split("\t")
			word = line[0]
			word_def = line[1]
			words_and_defs.append([word, word_def])

		# break down the course/category/lesson to 
		# extract the lesson filename
		if (len(lesson_category) > 0):
			tmp = lesson_category.split(":")
			tmp = tmp[1].split("/")
			output_filename = "SSAT_Vocabulary_Builder_" + tmp[2] + ".txt"

	return [words_and_defs, output_filename, lesson_category]

#################################################################
# Method:		write_output(arglist)
#
# Description:	Write the output file
#
# Arguments:	arglist - list containing the words/definitions
#						  list, the output filename, and the
#						  Moodle/GIFT $CATEGORY header.
#
# Returns:		None
#################################################################
def write_output(arglist):

	print("\nCreating output file: " + arglist[1] + "\n")
	output = open(arglist[1], "w")

	# write the data in GIFT import format
	output.write(arglist[2] + "\n\n")
	output.write("[html]\n")
	output.write("Match the words with their meanings. {\n")
	for item in arglist[0]:
		output.write(item[0] + " -> " + item[1] + "\n")
	output.write("}")

	# Close Output stream
	output.close

#################################################################
#                        Main Program                           #
#################################################################

# load and transform input file contents into GIFT import format
# and create the output file based on the lesson name.
write_output(process_data(load_file(parse_args())))

# Exit Program
exit()