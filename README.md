# Ordered-Linked-Lists
Instructions
You will need to create four files:

Book.py - file containing a class definition for a Book object
BookCollection.py - file containing a class definition for a collection of Books that will be implemented as an Ordered Linked List
BookCollectionNode - file containing a class definition for a Node in the BookCollection
testFile.py - file containing pytest functions testing the overall correctness of your class definitions
There will be no starter code for this assignment, but rather the class descriptions and required methods are defined in the specification below.

You should organize your lab work in its own directory. This way all files for a lab are located in a single folder. Also, this will be easy to import various files into your code using the import / from technique shown in lecture.

Book.py class
The Book.py file will contain the definition of a Book. We will define the Book attributes as follows:

title - str that represents the title of the Book
author - str that represents the author of the Book. This will be in a LastName, FirstName format. You may assume this will always be the case
year - int that represents the year the Book was published
You should write a constructor that allows the user to construct a book object by passing in values for all of the fields. Your constructor should set the title and author attribues to empty strings (""), and the year attribute to None by default.

__init__(self, title, author, year)
In addition to your constructor, your class definition should also support “getter” methods that can receive the state of the Book object:

getTitle(self)
getAuthor(self)
getYear(self)
You will implement the method

getBookDetails(self)
that returns a str with all of the Book attributes. The string should contain all attributes in the following EXACT format (Note: There is no \n character at the end of this string):

b = Book("Ready Player One", "Cline, Ernest", 2011)
print(b.getBookDetails())
Output

Title: Ready Player One, Author: Cline, Ernest, Year: 2011
Lastly, your Book class will overload the > operator (__gt__). This will be used when finding the proper position of a Book in the Ordered Linked List using the specification above. We can compare books using the > operator while walking down the list and checking if the inserted book is > than a specific Book in the Ordered Linked List.
We reviewed operator overloading in class and the textbook does discuss overloading Python operators. You can also refer to this reference on overloading various operators as well:

https://www.geeksforgeeks.org/operator-overloading-in-python/

BookCollection.py and BookCollectionNode.py
The BookCollectionNode.py file will define the BookCollectionNode class. This will be similar to the Linked List Node implementation done in lecture. You will need to write the following methods:

__init__(self, data) - constructor that will assign the parameter data (a Book object) as part of this node. Each node will also have a next reference associated with it. When constructing a BookCollectionNode, the next reference should be None by default
getData(self) - getter method that returns the data (Book object)
getNext(self) - getter method that returns the next BookCollectionNode in the Linked List structure
setData(self, newData) - updates the Node’s data with the parameter newData
setNext(self, newNext) - updates the Node’s next reference with the newNext parameter (another BookCollectionNode)
The BookCollection.py file will contain the definition of a collection of Book objects stored in an Ordered Linked List. The BookCollection will manage an Ordered Linked List containing BookCollectionNodes.The BookCollection class will be responsible for maintaining the overall structure of the Ordered Linked List. Your BookCollection class will need to support the following methods:

__init__(self) - constructor that will have a head reference that references the first node in the Ordered Linked List. This should be set to None by default.
isEmpty(self) - method that returns True (boolean) if the BookCollection is empty, and returns False otherwise
getNumberOfBooks(self) - method that returns the total number of Books (int) in the BookCollection
insertBook(self, book) - method that inserts a Book in the appropriate place. As mentioned before, all Books in the BookCollection are ordered based on 1) the Book’s author (alphabetical / lexicographical order), then 2) the Book’s year of publication, and then 3) the Book’s title (alphabetical / lexicographical order). Here is where we can utilize the Book’s > operator. You’ll need to do some logic to replace the references for the BookCollectionNodes when inserting the Book in the appropriate place.
getBooksByAuthor(self, author) - method that returns a str containing all of the Book details by a specified author. Note that each book will be in its own line (each line ending with a \n character). Also note that the input parameter (author) may be in a different case than the case of the author that the book was constructed with - in this situation, the comparison of the authors’ names should be case insensitive (‘a’ == ‘A’). An example (with correct order) is shown below:
b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)
print(bc.getBooksByAuthor("KING, Stephen"))
Output:

Title: Rage, Author: King, Stephen, Year: 1977
Title: The Shining, Author: King, Stephen, Year: 1977
Title: Cujo, Author: King, Stephen, Year: 1981

getAllBooksInCollection(self) - method that returns a str containing the details of all Books in the BookCollection. Note that each book will be in its own line (each line ending with a \n character). An example (with correct order) is shown below:
b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)
print(bc.getAllBooksInCollection())
Output:

Title: Ready Player One, Author: Cline, Ernest, Year: 2011
Title: Rage, Author: King, Stephen, Year: 1977
Title: The Shining, Author: King, Stephen, Year: 1977
Title: Cujo, Author: King, Stephen, Year: 1981

removeAuthor(self, author) - method that removes all Books written by a specified author. Since this is an Ordered Linked List, all Books written by a specific author should be located right next to each other in the Book Collection assuming your insertBook method has been implemented correctly. Note: the input parameter (author) may be in a different case than the case of the author that the book was constructed with - your solution must account for these situations.
recursiveSearchTitle(self, title, bookNode) - method that searches the BookCollection for a specific Book title passed in the method. Note: this method must be done recursively. This method will return True if a Book in the BookCollection has the same title as the parameter title (str), and return False otherwise.
Since this solution is recursive, this method will take in a reference to a BookCollectionNode object (bookNode) in the BookCollection that needs to be searched.
The initial call to recursiveSearchTitle would pass in the head of the BookCollection since that’s the starting point to search through the entire BookCollection. For example:
  b0 = Book("Cujo", "King, Stephen", 1981)
  b1 = Book("The Shining", "King, Stephen", 1977)
  bc = BookCollection()
  bc.insertBook(b0)
  bc.insertBook(b1)
  assert bc.recursiveSearchTitle("CUJO", bc.head) == True
  assert bc.recursiveSearchTitle("Twilight", bc.head) == False
You can then recursively search through the BookCollection sub parts by recursively referring to the next BookCollectionNode in BookCollection that needs to be searched if the Book in bookNode does not have the title we’re looking for.
Note: the input parameter title may be in a different case than the case of the title that the Book was constructed with - your solution must account for these situations (see assert statement above).
