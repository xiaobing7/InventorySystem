
import inventory_client


def get_book_titles(client, isbns):
    titleList = []
    for isbn_input in isbns:
        response = client.get_book_by_isbn(isbn_input)
        titleList.append(response.book.title)

    return titleList


if __name__ == '__main__':
    titles = get_book_titles(inventory_client.Client(), ["ISBN9780553393965", "ISBN9781335425751"])
    print(titles)
