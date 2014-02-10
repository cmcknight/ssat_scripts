"""
	Program:	Moodle GIFT Generators

	Author:		C. McKnight

	Description:
		The following methods generate a GIFT-formatted file for
		the Moodle 2 learning system to import into its question
		bank.
"""

#####################################################################
# imports
#####################################################################
import sys

#####################################################################
# methods
#####################################################################

#====================================================================

def wordmatch_generator(wordbank, outfile):
	"""Generate word match quiz

		This method generates a GIFT-formatted word match quiz.

		Args:
			wordbank	dictionary of words and definitions
			outfile 	output file handle

		Returns:
			None
	"""			
	outfile.write("Match the words with their meanings. {\n")
	
	# walk the word bank and generate the GIFT formatted output
	for key in wordbank:
		outfile.write("=" + key + " -> " + wordbank[key]['definition'] + "\n")
	outfile.write("}")

#====================================================================

def fill_in_the_blank_generator(wordbank, outfile):
	"""Generates a GIFT-formatted fill in the blank quiz.

		This method generates a GIFT-formatted fill in the blank quiz
		from the provided wordbank.

		Args:
			wordbank	dictionary of words and sentences
			outfile 	output file handle

		Returns:
			None
	"""
	# extract the keys and sort them
	keys = wordbank.keys()
	keys = sorted(keys)
	
	# iterate over the dictionary and write the entries to the output file
	for wordkey in wordbank:
		sentence = wordbank[wordkey]['sentence'].split("{}")
		outfile.write(sentence[0] + "{\n")
		for answerkey in keys:
			if answerkey == wordkey:
				leader = "="
			else:
				leader = "~"
			outfile.write(leader + answerkey + "\n")
		outfile.write("}" + sentence[1] + "\n\n")

#====================================================================

def generate_quiz(databank, quiztype):
	"""Generates a GIFT-formatted import file for Moodle 2

		This method takes a dictionary of information and writes its
		as a GIFT-formatted import file for Moodle 2.

		Args:
			databank - 	Dictionary containing the Moodle header info
					  	and the wordbank.
			quiztype - 	Type of quiz to generate

		Returns:
			None
	"""

	# Create Moodle import file header
	course = databank['Moodle GIFT Header']['course']
	category = databank['Moodle GIFT Header']['category']
	lesson = databank['Moodle GIFT Header']['lesson']
	header = "$CATEGORY: " + course + "/" + category + "/" + lesson + "\n\n[html]\n"
	output_filename = lesson
	if (quiztype == 'wordmatch'):
		output_filename = output_filename + "-Matching"
	elif (quiztype == 'fillblank'):
		output_filename = output_filename + '-FillInTheBlank'
	output_filename = output_filename + ".txt"
	output_filename = output_filename.replace(" ", "_")  # eliminate spaces in filenames

	# open the output file
	with open(output_filename, 'w') as output:
		# write the header
		output.write(header)

		if quiztype == 'wordmatch':
			wordmatch_generator(databank['wordbank'], output)
		elif quiztype == 'fillblank':
			fill_in_the_blank_generator(databank['wordbank'], output)
		else:
			print("Invalid quiz type!")
		output.close()

#====================================================================

