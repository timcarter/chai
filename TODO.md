## Components of a citation
* Authors
	* The first author will have the last name and first name separated by a comma. If there are no other authors, then a period will occur next.
	* Two authors will be separated by an "and".
	* All authors other than the first will have the first name come first.
	* I have no idea how East Asian names are displayed.
	* Assume full names for everyone, not just et. al. This parser does not try to parse the notes section, only the bibliography.
* Translaters, editors, compilers
	* Distinguished by a title coming after the name (trans., translator, ed., etc.).
	* There is an additional possibility that a separate statement will say "Translated by..." or "Edited by...".
* Titles
	* The title of a book or major work will be in italics.
	* Articles and shorter pieces will be quotes.
	* The phrase "in {{TITLE}}" will exist for shorter pieces.
* Page Numbers
	* Exist only for shorter pieces; usually comes in the same statement as the editors.
	* Might be roman numerals.
* Year of publication
	* Exists in the publishing cities statement.
	* Might be confused with the page number.

## Algorithm
	* O(n)|n=length of the statement: run through the entire citation and try to identify individual statements.
	* Create modules for each component of the citation and try to find those by regular expression (or something else).
