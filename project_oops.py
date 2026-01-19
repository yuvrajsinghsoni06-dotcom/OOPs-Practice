from abc import ABC, abstractmethod
class LibraryItems(ABC):
    def __init__(self, title , item_id):
        self._title = title
        self._item_id = item_id
    @abstractmethod
    def checkout(self):
        pass
    @abstractmethod
    def return_items(self):
        pass
class Book(LibraryItems):
    def __init__(self , title , item_id , author):
        super().__init__(title , item_id)
        self._author = author
        self._is_checked_out = False
    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f'Book {self._title} by {self._author}')
            return True
        else:
            print(f'Book {self._title} is already checked out.')
            return False
    def return_items(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f'Book {self._title} returned.')
            return True
        else:
            print(f'Book {self._title} was not checked out.')
            return False
class Ebook(LibraryItems):
        def __init__(self , title , item_id , file_size):
            super().__init__(title, item_id)
            self.file_size = file_size
        def checkout(self):
            print(f"Dowloading {self._title} of size {self.file_size}MB...")
            return True
        def return_items(self):
            print(f"Removing {self._title} from your device...")
            return True
library = [Book("Atomic habits" , 101 , "james clear") , Ebook("Deep work" , 102 , 5)]  
for books in library:
    books.checkout()
    books.return_items()    

