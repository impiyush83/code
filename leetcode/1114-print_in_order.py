from threading import Lock


class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()