import book
from unittest import TestCase

monaLisa = book.Book("MonaLisa.json")
monaLisa.openBook()
book = monaLisa.getBook()
#print(book["pages"]["1"][2])
print(monaLisa.getPage("1"))