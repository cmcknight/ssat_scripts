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
#                        Main Program                           #
#################################################################

# default the input file to the system standard input stream
input_file = sys.stdin

# Parse the command line options
args = parse_args()

# assign to associated variables
filename = args['f']
delimiter = args['d']

# open the input stream
if (filename != '-'):
	try:
		input_file = open(filename, 'r')
	except IOError:
		print("I'm sorry, the file [" + filename + "] does not exist.")

#################################################################
# Processing loop - process all file data                       #
#################################################################

# load file contents
lines = input_file.readlines()
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

# Close the input stream
input_file.close

# break down the course/category/lesson to extract the lesson filename
if (len(lesson_category) > 0):
	tmp = lesson_category.split(":")
	tmp = tmp[1].split("/")
	output_filename = "SSAT_Vocabulary_Builder_" + tmp[2] + ".txt"
	print(output_filename)

# Open output stream and write output file
output = open(output_filename, "w")

output.write(lesson_category + "\n\n")
output.write("[html]\n")
output.write("Match the words with their meanings. {\n")
for item in words_and_defs:
	output.write(item[0] + " -> " + item[1] + "\n")
output.write("}")

# Close Output stream
output.close

# Exit Program
exit