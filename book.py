# Imports
import json

class Book():
    '''This class contains the book in JSON format'''
    book = None

    def __init__(self, filename):
        '''Constructor for book class'''
        self.filename = filename

    def openBook(self):
        '''Loads book from provided filename'''
        try:
            with open(self.filename, "r") as file:
                self.book = json.load(file)
        except FileNotFoundError:
            print(f"Error: File not Found: {self.filename}")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {self.filename}")
        except Exception as e:
            print(f"Error: Unexpected Error: {e}")

    def getBook(self):
        """ getBook returns the book """
        return self.book
    
    def getPage(self, pageNum):
        """ getPage gets the selected page """
        if type(pageNum) != str:
            pageNum = str(pageNum)

        return self.book["pages"][pageNum]
