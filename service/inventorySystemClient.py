import logging

import grpc
import inventory_pb2
import inventoryService_pb2
import inventoryService_pb2_grpc


def get_book_by_isbn(stub, isbn_input):
    return stub.GetBook(inventoryService_pb2.BookSearchRequest(isbn=isbn_input))


def create_book(stub, book):
    return stub.CreateBook(inventoryService_pb2.BookCreateRequest(book=book))


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)

        print(">>>>>>>>>>>>>>>Get book by correct isbn<<<<<<<<<<<<<<<<<<<<<<<<<<")
        isbn = "ISBN9781571314710"
        get_book_response1 = get_book_by_isbn(stub, isbn)
        print("Client received: " + str(get_book_response1))

        print(">>>>>>>>>>>>>>>Create Book Successfully<<<<<<<<<<<<<<<<<<<<<<<<<<")
        book = inventory_pb2.Book()
        book.isbn = "ISBN9781501127625"
        book.title = "Steve Jobs"
        book.author_name = "Walter Isaacson"
        book.genre = "BIOGRAPHY"
        book.publish_year = 2011
        create_book_response = create_book(stub, book)
        print("Client received after create a book: " + str(create_book_response))

        print(">>>>>>>>>>>>>>>Create a Book already exist<<<<<<<<<<<<<<<<<<<<<<<<<<")
        book1 = inventory_pb2.Book()
        book1.isbn = "ISBN9781501127625"
        book1.title = "Steve Jobs"
        book1.author_name = "Walter Isaacson"
        book1.genre = "BIOGRAPHY"
        book1.publish_year = 2011
        create_book_response = create_book(stub, book1)
        print("Client received after create a book: " + str(create_book_response))


if __name__ == '__main__':
    logging.basicConfig()
    run()
