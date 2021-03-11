from src.book_collector import BookCollector
from src.file_manager import FileManager

book_collector = BookCollector()
books = book_collector.books
FileManager.set_output(books)
