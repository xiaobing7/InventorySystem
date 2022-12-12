import inventoryService_pb2

def CreateBookService(book):
    book = inventoryService_pb2.book__pb2.Book()
    book.isbn = "1345"