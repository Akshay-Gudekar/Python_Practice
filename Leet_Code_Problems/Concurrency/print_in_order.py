import threading
from typing import Callable


class Foo:
    def __init__(self):
        # We use Events because they are like simple on/off switches
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        # "Set" the event to True (Open the first gate)
        self.first_done.set()

    def second(self, printSecond: Callable[[], None]) -> None:
        # Wait here until first_done.set() is called
        self.first_done.wait()
        printSecond()
        # Open the second gate
        self.second_done.set()

    def third(self, printThird: Callable[[], None]) -> None:
        # Wait here until second_done.set() is called
        self.second_done.wait()
        printThird()



def print_first(): print("first", end=" ")


def print_second(): print("second", end=" ")


def print_third(): print("third", end=" ")


if __name__ == "__main__":
    foo = Foo()

    # We create the threads in the WRONG order to prove the code works
    # Even though 'third' is started first, it will wait.
    t3 = threading.Thread(target=foo.third, args=(print_third,))
    t2 = threading.Thread(target=foo.second, args=(print_second,))
    t1 = threading.Thread(target=foo.first, args=(print_first,))

    t3.start()
    t2.start()
    t1.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()