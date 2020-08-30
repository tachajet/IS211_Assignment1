class Book(object):
	"""Class that creates book objects with author and title strings
"""
	author=""
	title=""
	def __init__(self,author,title):
		self.author=author
		self.title=title
	def display(self):
		"""function to print authors and titles from Book class instances
"""
		print(self.title, "written by", self.author)
stein=Book("John Steinbeck","Of Mice and Men")
harp=Book("Harper Lee", "To Kill A Mockingbird")
stein.display()	
harp.display()	
