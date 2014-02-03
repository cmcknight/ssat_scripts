#Complete The Sentence Design Document

-----------------------------------------------------------------------------

##Overview

This script takes a delimited text file as its input and exports a GIFT-formatted text file as an output. The user may specify the filename on the command line or use the pipe operator to send the contents of the file through the standard input stream.The user may specify the delimiter with the TAB character used as the default.

-----------------------------------------------------------------------------

##Sample File
<pre>SSAT Vocabulary/Vocabulary Builder/Lesson_5B\<newline\><br />abated\<tab\>lessened; eased\<newline\><br />apocalypse\<tab\>total devastation, the end of the world\<newline\></pre>

The first line in the data file should contain the path hierarchy for the following lines. This line is the header line for the GIFT format and will be inserted as the first line in the output file. The lesson name will be used as the output file name as well.

The format for the first line is:

<pre>$CATEGORY: \<Course Name\>/\<Category\>/\<Lesson Name\></pre>

All lines after the first line are in the format:
<pre>\<word\>\<delimiter\>\<definition\></pre>

-----------------------------------------------------------------------------

##GIFT Format

The header for the file will have the following format and is copied from the input file:

<pre>$CATEGORY: Course Name/Category Name/Lesson Name</pre>

A generic sentence will be created for each word in the word list. The insertion point for the word will be just before the closing period for the sentence. The initial iteration will require the question author to write a sentence and shift the insertion point. Future iterations will allow for the creation of sentences ahead of time that will merged into the proper GIFT formatted output.

Lorem ipsum dolor {
~word1
~word2
=word3
~word4
}.

The tilde (~) indicates an invalid answer. The equal sign (=) indicated the correct answer.

-----------------------------------------------------------------------------

##Command Line Specification

complete_the_sentence [-h] [-d delimiter] [-f filename]

<table>
	<tr>
		<td><b>-h</b></td><td>Help</td>
	<tr>
		<td><b>-d</b></td><td>Delimiter character</td>
	</tr>
	<tr>
		<td><b>-f</b></td><td>optional name of input file; defaults to standard input</td>
	</tr>
</table>

The default behavior is to accept input from the standard system input stream (stdin) via redirection.

-----------------------------------------------------------------------------

##Program Execution Plan

1. Parse command line options
2. Open input stream (using the system standard input stream if no filename is specified with the -f switch)
3. Load file contents
4. Parse line of data
5. Validate Data 
	1. Determine if the line is empty. If so, log, discard and repeat step 1.
	2. If first line, determine if the line is properly formatted (has "$CATEGORY:" followed by course, category and lesson entry.). If not, log the line and repeat step 1.
	3. If not first line, determine if the line is properly formatted (has an entry, a delimiter, and another entry). If not, log the line and repeat step 1.5. Store word / definition 
7. If not end of file, repeat steps 1-3
8. Write GIFT-formatted file
9. Close all streams.

-----------------------------------------------------------------------------

##Implementation History

<table>
	<tr>
		<th>Version</th><th>Released</th><th>Description</th>
	</tr>
	<tr>
		<td>1.0</td><td>2 February 2014</td><td>Initial version</td>
	</tr>
</table>

-----------------------------------------------------------------------------

##Roadmap

<table>
	<tr>
		<th>Version</th><th>Status</th><th>Comments</th>
	</tr>
	<tr>
		<td>1.0</td>
		<td>Complete</td>
		<td>Create initial file with generic sentence placeholder.</td>
	</tr>
	<tr>
		<td>1.1</td>
		<td>In Design</td>
		<td>Use custom input file with sentences. Word appearance marked by placeholders</td>
	</tr>
</table>