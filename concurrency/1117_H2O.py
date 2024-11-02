import threading
from typing import Callable

class H2O:
    def __init__(self):
        self.h_sem = threading.Semaphore(2)
        self.o_lock = threading.Lock()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.h_sem._value == 0 and self.o_lock.locked():
            self.o_lock.release()
            self.h_sem.release()
            self.h_sem.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_lock.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        if self.h_sem._value == 0:
            self.o_lock.release()
            self.h_sem.release()
            self.h_sem.release()
