class FlatIterator_2:

    def __init__(self, list_of_list):
        self.stack = list(list_of_list)

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            item = self.stack.pop(0) 
            if isinstance(item, list):
                self.stack = item + self.stack
            else:
                return item
        raise StopIteration

