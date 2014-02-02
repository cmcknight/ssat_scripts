# ############################
# Program:		word_match.py
# Version:		1.0
# ############################

#################################################################
# Imports
#################################################################
import argparse, sys

#################################################################
# Function: 	parse_args
#
# Arguments:	None
#
# Returns:		Dictionary with argument values
#
# Description:
#
# 	The parse_args method returns a dictionary with all of the
# 	command line arguments associated with the full name of each
#	argument.
#################################################################

#################################################################
# parse the command line arguments                              #
#################################################################
def parse_args():
	# create an instance of an argparse object
	parser = argparse.ArgumentParser(description='Process text files for word match GIFT output.')

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
	#sysargs = sys.argv
	ns = parser.parse_args()

	# determine whether to use the provided file name or standard input stream
#	try:
#		ns.input_file = open(ns.f, 'r')
#		parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
	
#	except IOError:
#		print("Can't open [" + ns.f + "]. Defaulting to stdin.")
#		input_file = sys.stdin

	args = dict()
	args = vars(ns)
	return args

#################################################################
# load the file contents
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
			print("I'm sorry, the file [" + filename + "] does not exist.\n")
			print("******************* Error ********************\n")
			exit()

	# load the file into a list
	lines = input_file.readlines()

	# close the file
	input_file.close()

	return lines

#################################################################
# Process the file contents
#################################################################
def process_data(data):
	words_and_defs = list()

	# loop over the file contents
	lesson_category = ""
	for line in lines:
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

		# break down the course/category/lesson to extract the lesson filename
		if (len(lesson_category) > 0):
			tmp = lesson_category.split(":")
			tmp = tmp[1].split("/")
			output_filename = "SSAT_Vocabulary_Builder_" + tmp[2] + ".txt"

	return words_and_defs, output_filename, lesson_category

#################################################################
# write the output file
#################################################################
def write_output(wordlist, filename, category):
	print("\nCreating output file: " + filename + "\n")
	output = open(filename, "w")

	output.write(category + "\n\n")
	output.write("[html]\n")
	output.write("Match the words with their meanings. {\n")
	for item in wordlist:
		output.write(item[0] + " -> " + item[1] + "\n")
	output.write("}")

	# Close Output stream
	output.close

#################################################################
#                        Main Program                           #
#################################################################

# parse the command line options
args = parse_args()

# load file contents
lines = load_file(args)

# process file data
mylist, filename, category = process_data(lines)

# open output stream and write output file
write_output(mylist, filename, category)
# Exit Program
exit