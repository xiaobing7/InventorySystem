import unittest
from unittest.mock import MagicMock

from client.get_book_titles import get_book_titles
from service import inventory_pb2
from service import inventoryService_pb2
import inventory_client

mock_client = MagicMock()

mock_client.get_book_by_isbn.side_effect = [
    inventoryService_pb2.BookSearchResponse(
        book=inventory_pb2.Book(isbn="ISBN00001", title="Bright Dead Things",
                                author_name="Milkweed Editions", genre="POETRY", publish_year=2015)),
    inventoryService_pb2.BookSearchResponse(book=inventory_pb2.Book(isbn="ISBN00002",
                                                                    title="And There Was Light: Abraham Lincoln and the American Struggle",
                                                                    author_name="Jon Meacham",
                                                                    genre="HISTORY", publish_year=2022))
]


class TestService(unittest.TestCase):
    def test_get_book_titles_func(self):
        res = get_book_titles(mock_client, ["ISBN00001", "ISBN00002"])
        self.assertEqual(res, ["Bright Dead Things", "And There Was Light: Abraham Lincoln and the American Struggle"])

    def test_get_book_titles_func_with_server(self):
        client = inventory_client.Client()
        titles = get_book_titles(client, ['ISBN9780553393965', 'ISBN9781335425751'])
        self.assertEqual(titles, ["And There Was Light: Abraham Lincoln and the American Struggle", "Beach Wedding"])


if __name__ == '__main__':
    unittest.main()
