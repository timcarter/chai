import sys
import webbrowser
import os
import re

citation = 'Pollan, Michael. <i>The Omnivore\'s Dilemma: A Natural History of Four Meals</i>. New York: Penguin, 2006.'

# check for "Accessed [Date]"

# try to find the publisher information. ideally publisher_information will only have one element
# if it has more than one, then we're in uncharted territory
publisher_information = []
map(
	lambda publisher_segment : publisher_information.append(publisher_segment),
	re.compile (r"(([a-zA-Z\s]+?):\s*([^,\.]+),\s*(\d+).)").findall(citation)
)

if len(publisher_information) == 0:
	print 'No publisher information found in citation'
if len(publisher_information) == 1:
	print 'City: ' + publisher_information[0][1]
	print 'Publisher: ' + publisher_information[0][2]
	print 'Year: ' + publisher_information[0][3]
	citation = citation.replace(publisher_information[0][0], '')
elif len(publisher_information) > 1:
	print 'More than one publisher was found'
	print publisher_information

print 'CITATION: ' + citation

# find the title of the work
title_re_results = re.compile('(\<i\>(.+)\<\/i\>.)').findall(citation)

if len(title_re_results) == 1:
	print title_re_results[0][1]
	citation = citation.replace(title_re_results[0][0], '')
else:
	print 'Something went wrong deciphering the title: '
	print title_re_results

print 'CITATION II: ' + citation

# find the author


