class BookShelf():
	def __init__(self, *books) -> None:
		self.books = books

	def __str__(self) -> str:
		return f"BookShelf with {len(self.books)} books."
	
	def print(self):
		print([str(book) for book in self.books])
	
class Book():

	def __init__(self, name) -> None:
		self.name = name

	def __str__(self) -> str:
		return f"Book {self.name}"


book1 = Book("Harry Potter")
book2 = Book("Python 101")

book_shelf = BookShelf(book1, book2)

print(book_shelf)
book_shelf.print()