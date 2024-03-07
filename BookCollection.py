from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def getNumberOfBooks(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.getNext()
        return count
    def insertBook(self, book):
        new_node = BookCollectionNode(book)
        current_node = self.head
        previous_node = None
        while current_node != None and book > current_node.getData():
            previous_node = current_node
            current_node = current_node.getNext()
        if previous_node == None:
            self.head = new_node
            new_node.setNext(current_node)
        else:
            previous_node.setNext(new_node)
            new_node.setNext(current_node)
    def getBooksByAuthor(self, author):
        author = author.lower()
        result = ''
        current_node = self.head
        while current_node != None:
            if current_node.getData().getAuthor().lower() == author:
                result += current_node.getData().getBookDetails() + "\n"
            current_node = current_node.getNext()
        return result
    def getAllBooksInCollection(self):
        result = ''
        current_node = self.head
        while current_node != None:
            result += current_node.getData().getBookDetails() + "\n"
            current_node = current_node.getNext()
        return result
    def removeAuthor(self, author):
        author = author.lower()
        current_node = self.head
        previous_node = None
        while current_node != None:
            if current_node.getData().getAuthor().lower() == author:
                if previous_node == None:
                    self.head = current_node.getNext()
                else:
                    previous_node.setNext(current_node.getNext())
            else:
                previous_node = current_node
            current_node = current_node.getNext()
    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        if bookNode.getData().getTitle().lower() == title.lower():
            return True
        return self.recursiveSearchTitle(title, bookNode.getNext())
