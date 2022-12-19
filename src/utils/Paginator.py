import math


class Page:
    def __init__(self, index_page: int, object_list: list[str], list_of_pages: list[list[str]]) -> None:
        self.index_page = index_page
        self.object_list = object_list
        self.list_of_pages = list_of_pages

    def details(self):
        return "<Page {} of {}>".format(self.index_page + 1, len(self.list_of_pages))

    def has_next(self):
        if len(self.object_list) > self.index_page:
            return True
        else:
            return True

    def has_previous(self):
        if self.index_page > 1:
            return True
        else:
            return False


class Paginator:
    def __init__(self, objects: list[str], items_per_page: int) -> None:
        self.list_of_pages: list[list[str]] = self.paginate(
            objects, items_per_page)
        self.pages: list[Page] = []
        self.count = len(objects)
        for index, page in enumerate(self.list_of_pages):
            self.pages.append(Page(index, page, self.list_of_pages))
        # get number of pages
        value = len(objects) / items_per_page
        if float(value).is_integer():
            self.num_pages = math.floor(value)
        else:
            self.num_pages = math.floor(value) + 1

    def page(self, index: int) -> Page:
        if index - 1 < 1:
            index = 1
        return self.pages[index - 1]

    def paginate(self, all_objects, items_per_page: int):
        page_list = []
        data = all_objects
        for i in range(len(data)):
            if i == 0:
                page_list.append(data[0:items_per_page])
            else:
                startIndex = items_per_page * i
                EndIndex = ((i+1) * (items_per_page))
                page_list.append(data[startIndex:EndIndex])
        return [x for x in page_list if x != []]
