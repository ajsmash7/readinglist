from dataclasses import dataclass, field

# TODO add a docstring for this module.

''' This Module contains the object class models to create an instance of:
 
 a counter object
 a book object 
 
This module defines the data classes and their class methods as a model for use in book list application. '''


def gen_id():
    return Counter.get_counter()


class Counter:
    # TODO add a docstring for this class to explain it's purpose
    '''
    This class creates an instance of a counter object and defines
    class methods for use with counter objects

    - it is initialized with a value of zero

    - when the get_counter method is called, one is added to the counter
    current counter instance and returned

    - reset_counter sets the value back to zero for the current instance
    '''

    _counter = 0

    @staticmethod
    def get_counter():
        Counter._counter += 1
        return Counter._counter

    @staticmethod
    def reset_counter():
        Counter._counter = 0


@dataclass
class Book:

    # TODO add a docstring for this class to explain it's purpose
    '''
    This class instantiates a new Book object.

    It defines the properties that are required to make a book

    It sets the default for the generated value of id, which is calls the
    counter function above to generate.

    Every book has a title and an author

    It sets the default for the value of read, because if you are adding it to
    the list, it's because you have not read the book yet.

    lastly, it creates the toString class method to display the property values
    of the referenced instance as a string.
    '''

    id: int = field(default_factory=gen_id, init=False)
    title: str
    author: str
    read: bool = False

    def __str__(self):
        read_status = 'have' if self.read else 'have not'
        return f'ID {self.id}, Title: {self.title}, Author: {self.author}. You {read_status} read this book.'
