#Word Match Design Document

##Overview

This script expects a delimited file to be piped in as its input and
exports a GIFT-formatted file as an output. The user may specify the
delimiter with the TAB character used as the default.

##Sample File Entry

abated\<tab\>lessened; eased\<newline\>


##GIFT Format

The header for the file will have the following format:

<pre>$CATEGORY: Course Name/Category Name/Lesson Name</pre>

One entry per word will be created with the following format:

<pre>Match the words with their meanings. {
	=abated -> lessened; eased\<newline\>
	=apocalypse -> total devastation, the end of the world\<newline\>
	etc.
}</pre>

##Command Line Specification

word_match.py [-d\<delimiter\>] -C\<course\> -c\<category\> -q\<quiz name\>

-d     Delimiter character

##Program Execution Plan

1. Parse command line options
2. Open input stream (using the system standard input stream)
3. Parse 1st line
4. Validate Data 
	4.1. Determine if the line is empty. If so, log, discard and
		 repeat step 1.
	4.2. Determine if the line is properly formatted (has an entry, a
		 delimiter, and another entry). If not, log the line and 
		 repeat step 1.
5. Store word / definition 
6. If not end of file, repeat steps 1-3
7. Prompt User for Course / Category / Quiz Name
8. Write GIFT-formatted file
9. Close all streams.

