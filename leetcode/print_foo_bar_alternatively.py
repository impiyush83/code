from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = Lock()
        self.barlock = Lock()
        self.foolock.aquire()
        self.barlock.aquire()

    def printFoo(self):
        for i in range(0, 1):
            print("foo")

    def printBar(self):
        for i in range(0, 1):
            print("bar")

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.foolock:
                printFoo()
            self.foolock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.barlock:
                printBar()
            self.barlock.release()

a = FooBar(2)
