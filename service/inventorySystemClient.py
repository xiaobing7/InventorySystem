import logging

import grpc
import inventory_pb2_grpc
import inventory_pb2

def get_book(stub):
    return stub.GetBook(inventory_pb2.BookSearchRequest(title='Beach Wedding'))

def create_book(stub):
    book = inventory_pb2.Book()
    book.isbn = "ISBN9781501127625"
    book.title = "Steve Jobs"
    book.author_name = "Walter Isaacson"
    book.genre = "BIOGRAPHY"
    book.publish_year = 2011

    return stub.CreateBook(inventory_pb2.BookCreateRequest(book=book))

def run():
    with grpc.insecure_channel('localhost:50051') as channel:

        stub = inventory_pb2_grpc.InventoryServiceStub(channel)
        get_book_response = get_book(stub)
        print("Client received: " + str(get_book_response ))
        create_book_response = create_book(stub)
        print("Client received after create a book: " + str(create_book_response ))


if __name__ == '__main__':
    logging.basicConfig()
    run()
