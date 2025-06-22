#Implementing Basic OOP for a Library Management System
#system that tracks books in a library

class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self._is_checked_out = False # private attribute

	def check_out(self):
		if not self._is_checked_out:
			self._is_checked_out = True
			return True
		return False

	def return_book(self):
		if self._is_checked_out:
			self._is_checked_out = False
			return True
		return False

	def is_available(self):
		return not self._is_checked_out

class Library:
	def __init__(self):
		self.books = [] # private list of book objects

	def add_book(self, book):
		self._books.append(book)

	def check_out_book(self, title):
		for book in self.books:
			if book.title == title and book.is_available():
				book.check_out()
				return
		# optionally handle case where book is not found or already checked out

	def return_book(self, title):
		for book in self._books:
			if book.title = title and not book.is_available():
				book.return_book()
				return
		# optionally handle case where book is not found or already returned

	def list_available_books(self):
		for book in self._books:
			if book.is_available():
				print(f"{book.title} by {book.author}")
