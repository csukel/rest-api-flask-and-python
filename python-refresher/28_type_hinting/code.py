from typing import List #, Tuple, Set, etc...

# def list_avg(sequence: list) -> float:
#     """
#     This function is intended to be used for demonstration on how type hinting works in python
#     """
#     return sum(sequence) / len(sequence)


# f = list_avg([1, 2, 3])

class Book:
    pass


class BookShelf():
    def __init__(self, books: List[Book]) -> None:
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
    
