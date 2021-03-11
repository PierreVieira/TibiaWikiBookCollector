import requests
from bs4 import BeautifulSoup

from file_manager import FileManager


class BookCollector:
    def __init__(self):
        url = FileManager.get_url()
        html = requests.get(url=url)
        self.__soup = BeautifulSoup(html.content, 'html.parser')

    @property
    def books(self) -> "list[str]":
        all_td = self.__soup.select('td[width="250"]')
        books_name = []
        for td in all_td:
            if td.next:
                if td.next.name == 'a':
                    books_name.append(td.next.contents[0])
        return books_name