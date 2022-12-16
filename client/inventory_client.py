import logging
import sys

from service import inventoryService_pb2_grpc, inventoryService_pb2

import grpc


class Client(object):
    def __init__(self):
        logging.basicConfig()
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)

    def get_book_by_isbn(self, isbn_input):
        return self.stub.GetBook(inventoryService_pb2.BookSearchRequest(isbn=isbn_input))

    def create_book(self, book):
        return self.stub.CreateBook(inventoryService_pb2.BookCreateRequest(book=book))
