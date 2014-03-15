#SSAT Scripts

This repository contains a collection of scripts that convert text-based data files into GIFT format files suitable for uploading into Moodle.

## Vocabulary Data File Builder

This script takes a tab-delimited file as it's input and generates a JSON-formatted file used by the quiz builders below.

## Vocabulary Quiz Builders

###Word Match (word_match.py)

This script takes a delimited file in the form of **word**\<**delimiter**\>**definition** and convert them to a GIFT format file for matching words to definitions.

###Fill In The Blank (fill_in_the_blank.py)

This script takes a delimited file in the form of **word**\<**delimiter**\>**definition** and convert them to a GIFT format file for a fill in the blank quiz. A nonsense sentence is used with the embedded list of choices.
