from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    '''This annotation defines the method as abstract. It is
    best practice. An abstract method must be declared in the
    base class, but then must be defined in the inheriting classes. 
    '''
    @abstractmethod
    def display(): pass
class MyBook(Book):
	def __init__(self, title, author, price):
		self.title = title
		self.author = author
		self.price = price

	def display(self):
		print("Title:", self.title)
		print("Author:", self.title)
		print("Price:", self.price)