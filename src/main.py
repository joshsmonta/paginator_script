#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from utils.Paginator import Paginator

objects = [
    "Lauren Vickers",
    "Shazia Darby",
    "Zara Cain",
    "Edna Bradbury Parsons",
    "Clair Newton",
    "April Bruce Cain Kieran",
    "Timothy Bower",
    "Tracie Atkin Stanton",
    "Mabel Meadows",
    "Helen Rolfe",
    "Catriona Sampson"
]

items_per_page = 3


def main():
    """ Main entry point of the app """
    paginator = Paginator(objects, items_per_page)
    print(paginator.count)
    print(paginator.num_pages)

    page1 = paginator.page(1)
    print(page1.details())
    print(page1.object_list)
    print(page1.has_next())
    print(page1.has_previous())

    # print(paginator.list_of_pages)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
