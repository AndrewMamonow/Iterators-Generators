class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.counter = 0
        self.counter_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter_2 >= len(self.list[self.counter]):
            self.counter += 1
            self.counter_2 = 0
            if self.counter >= len(self.list):
                raise StopIteration
        item = self.list[self.counter][self.counter_2]
        self.counter_2 += 1            
        return item