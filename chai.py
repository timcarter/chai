# Citation: A class that represents a Chicago-style citation.
# The class accepts a full (hopefully syntactically valid) citation
# in the constructor and parses it once a property is requested--
# or you can just call parse. Keep in mind that this class assumes
# that the citations follow the "Notes and Bibliography" style normally
# used by historians and other humanists. If you're interested in parsing
# the "Author and Date" style you've come to the wrong place, at least until
# I write a parser for that as well.
class Citation:
	def __init__(self, citation):
		self.__fullCitation = citation
		self.__authors = []
		self.__editors = []
		self.translators = []
		self.__title = ''
		self.__publicationDates = []
		self.__publisher = ''
		self.__cityOfPublication = ''
		self.__dateAccessed = '' # timestamp
		self.__url = ''
		self.__originalPublishedWork = '' # reference to another work
		self.__containingWork = '' # object reference to a containing work
		self.__introducedWork = '' # object reference to the work of which this is an introduction
		self.__pages = '' # probably of format similar to: "297-301,333,345-346"
		self.__doi = ''
		self.__isDissertation = False
		self.__dissertationYear = 0
		self.__dissertationLocation = '' # usually a college
		self.__dissertationType = 'PhD' # could be MA or MS too
		self.__newspaper = '' # eg. The New York Times
		self.__conference = ''
		self.__conferenceLocation = ''
		self.__conferenceYear = ''
		self.__reviewedWork = '' # object reference to the work being reviewed
		self.__lastModifiedDate = ''

class Work(object):
	def __init__(self, authors=[], title='')
		self.__authors = authors
		self.__title = title

	def Authors(self, authors=None):
		if authors != None:
			self.__authors = authors

		return self.__authors

	def Title(self, title=None)
		if title != None:
			self.__title = title

		return title


class Book(Work):
	def __init__(self, authors=[], editors=[], title='', publisher='', publicationYear=None, publicationCity=''):
		super(Book, self).__init__(authors, title)

		self.__editors = editors
		self.__publisher = publisher
		self.__publicationYear = publicationYear
		self.__publicationCity = publicationCity

	def Editors(self, editors=None):
		if editors != None:
			self.__editors = editors

		return self.__editors

	def Publisher(self, publisher=None):
		if publisher != None:
			self.__publisher = publisher

		return self.__publisher

	def PublicationYear(self, publicationYear=None):
		if publicationYear != None:
			self.__publicationYear = publicationYear

		return self.__publicationYear

	def PublicationCity(self, publicationCity=None):
		if publicationCity != None:
			self.__publicationCity = publicationCity

		return self.__publicationCity

class Essay(Work):
	def __init__(self, authors=[], title='', containingWork=None, pages='', volume=''):
		super(Essay, self).__init__(authors, title)

		self.__containingWork = containingWork
		self.__pages = pages
		self.__volume = volume

	def ContainingWork(self, containingWork=None):
		if containingWork != None:
			self.__containingWork = containingWork

		return containingWork

	def Pages(self, pages=None):
		if pages != None:
			self.__pages = pages

		return self.__pages

	def Volume(self, volume=None):
		if volume != None:
			self.__volume = volume

		return self.__volume

class Article(Work):
	def __init__(self, authors=[], title='', periodical='', date=''):
		super(Article, self).__init__(authors, title)

		self.__periodical = periodical
		self.__date = date

	def Periodical(self, periodical=None)
		if periodicial != None:
			self.__periodical = periodical

		return self.__periodical

	def Date(self, date=None)
		if date != None:
			self.__date = date

		return self.__date

class OnlineArticle(Article):
	def __init__(self, authors=[], title='', periodical='', date='', url='', dateAccessed=''):
		super(OnlineArticle, self).__init__(authors, title, periodical, date)

		self.__url = url
		self.__dateAccessed = dateAccessed

	def Url(self, url=None):
		if url != None:
			self.__url = url

		return self.__url

	def DateAccessed(self, dateAccessed=None):
		if dateAccessed != None:
			self.__dateAccessed = dateAccessed

		return self.__dateAccessed
