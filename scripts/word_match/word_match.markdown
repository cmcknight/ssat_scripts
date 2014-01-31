#Word Match Design Document

-----------------------------------------------------------------------------

##Overview

This script takes a delimited text file as its input and exports a GIFT-formatted text file as an output. The user may specify the filename on the command line or use the pipe operator to send the contents of the file through the standard input stream.The user may specify the delimiter with the TAB character used as the default.

-----------------------------------------------------------------------------

##Sample File
<pre>SSAT Vocabulary/Vocabulary Builder/Lesson_5C\<newline\><br />abated\<tab\>lessened; eased\<newline\><br />apocalypse\<tab\>total devastation, the end of the world\<newline\></pre>

The first line in the data file should contain the path hierarchy for the following lines. This line is the header line for the GIFT format and will be inserted as the first line in the output file. The lesson name will be used as the output file name as well.

The format for the first line is:

<pre>$CATEGORY: \<Course Name\>/\<Category\>/\<Lesson Name\></pre>

All lines after the first line are in the format:
<pre>\<word\>\<delimiter\>\<definition\></pre>

-----------------------------------------------------------------------------

##GIFT Format

The header for the file will have the following format and is copied from the input file:

<pre>$CATEGORY: Course Name/Category Name/Lesson Name</pre>

One entry per word will be created with the following format:

<pre>Match the words with their meanings. {
	=abated -> lessened; eased\<newline\>
	=apocalypse -> total devastation, the end of the world\<newline\>
	etc.
}</pre>

-----------------------------------------------------------------------------

##Command Line Specification

word_match.py [-d\<delimiter\>] [filename]

<table>
	<tr>
		<td><b>-d</b></td><td>Delimiter character</td>
	</tr>
	<tr>
		<td><b>filename</b></td><td>optional name of input file; defaults to standard input</td>
	</tr>
</table>

-----------------------------------------------------------------------------

##Program Execution Plan

1. Parse command line options
2. Open input stream (using the system standard input stream)
3. Parse line of data
4. Validate Data 
	1. Determine if the line is empty. If so, log, discard and repeat step 1.
	2. If first line, determine if the line is properly formatted (has "$CATEGORY:" followed by course, category and lesson entry.). If not, log the line and repeat step 1.
	3. If not first line, determine if the line is properly formatted (has an entry, a delimiter, and another entry). If not, log the line and repeat step 1.5. Store word / definition 
6. If not end of file, repeat steps 1-3
7. Write GIFT-formatted file
8. Close all streams.

-----------------------------------------------------------------------------
