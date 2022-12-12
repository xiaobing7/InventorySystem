import logging

import grpc
import inventory_pb2
import inventoryService_pb2
import inventoryService_pb2_grpc


def get_book(stub):
    return stub.GetBook(inventoryService_pb2.BookSearchRequest(isbn="ISBN9781571314710"))


def create_book(stub):
    book = inventory_pb2.Book()
    book.isbn = "ISBN9781501127625"
    book.title = "Steve Jobs"
    book.author_name = "Walter Isaacson"
    book.genre = "BIOGRAPHY"
    book.publish_year = 2011

    return stub.CreateBook(inventoryService_pb2.BookCreateRequest(book=book))


def run():
    with grpc.insecure_channel('localhost:50051') as channel:

        stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)
        get_book_response = get_book(stub)
        print("Client received: " + str(get_book_response))
        create_book_response = create_book(stub)
        print("Client received after create a book: " + str(create_book_response))


if __name__ == '__main__':
    logging.basicConfig()
    run()
