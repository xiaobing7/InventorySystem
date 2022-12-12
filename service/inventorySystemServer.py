import logging
from concurrent import futures

import grpc
import inventory_pb2
import inventoryService_pb2
import inventoryService_pb2_grpc


class InventoryServicer(inventoryService_pb2_grpc.InventoryServiceServicer):
    """
    The database use a list of book object to store books details
    """

    def __init__(self):

        self.db = []
        book1 = inventory_pb2.Book()
        book1.isbn = "ISBN9780553393965"
        book1.title = "And There Was Light: Abraham Lincoln and the American Struggle"
        book1.author_name = "Jon Meacham"
        book1.genre = "HISTORY"
        book1.publish_year = 2022

        book2 = inventory_pb2.Book()
        book2.isbn = "ISBN9781335425751"
        book2.title = "Beach Wedding"
        book2.author_name = "Michael Ledwidge"
        book2.genre = "FICTION"
        book2.publish_year = 2022

        book3 = inventory_pb2.Book()
        book3.isbn = "ISBN9781571314710"
        book3.title = "Bright Dead Things"
        book3.author_name = "Milkweed Editions"
        book3.genre = "POETRY"
        book3.publish_year = 2015

        self.db.append(book1)
        self.db.append(book2)
        self.db.append(book3)

    def GetBook(self, request, context):
        # Iterate list of books, to search isbn

        for book in self.db:
            if book.isbn == request.isbn:
                return inventoryService_pb2.BookSearchResponse(book=book)
        # if the book not exists
        return inventoryService_pb2.BookSearchResponse(None)

    def CreateBook(self, request, context):
        book_to_add = request.book
        if not book_to_add:
            return inventoryService_pb2.BookCreateResponse(message="Fail to create book, try again")
        for book in self.db:
            if book.isbn == book_to_add.isbn:
                return inventoryService_pb2.BookCreateResponse(message="The book already exists, try again")

        self.db.append(book_to_add)
        # to check if book added successfully manually
        print("book database after modified: ", self.db)
        return inventoryService_pb2.BookCreateResponse(message="Create book <%s> successfully" % book_to_add.title)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
