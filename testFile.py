from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection




"""
def test_Book():
    b1 = Book("Life", "Joe", 2023)
    b2 = Book("Harry Potter", "Rowling", 1985) 
    assert b1.getTitle() == "Life"
    assert b1.getAuthor() == "Joe"
    assert b1.getYear() == 2023
    assert b1.getBookDetails() == "Title: Life, Author: Joe, Year: 2023"
    assert b2 > b1
def test_BookCollectionNode():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    node = BookCollectionNode(b)
    assert node.getData() == b
    assert node.getNext() is None
def test_BookCollection():
    b1 = Book("Cujo", "King, Stephen", 1981)
    b2 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b1)
    bc.insertBook(b2)
    assert bc.getNumberOfBooks() == 2
    expected_output = "Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.getAllBooksInCollection() == expected_output
    author_output = "Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.getBooksByAuthor("KING, Stephen") == author_output
    bc.removeAuthor("KING, Stephen")
    assert bc.getNumberOfBooks() == 0
    assert bc.recursiveSearchTitle("Cujo", bc.head) == True

"""
