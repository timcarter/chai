import sys
import webbrowser
import os
import re

citation = 'Pollan, Michael. <i>The Omnivore\'s Dilemma: A Natural History of Four Meals</i>. New York: Penguin, 2006.'

# check for "Accessed [Date]"

# if not there, the easiest thing to figure out is the city, publisher, and date
publishers = []
map(
	lambda publisher_segment : publishers.append(publisher_segment.strip()),
	re.compile (r"[a-zA-Z\s]+?:\s*[^,\.]+,\s*\d{4}.").findall(citation)
)

print '\n'.join(publishers)
print citation
