from collections.abc import Iterable

class MyIterable(Iterable):
    def __iter__(self):
        my_list = [1, 2, 4, 3, 5]
        return iter(my_list)
    
my_iterable = MyIterable()

for item in my_iterable:
    print(item)
