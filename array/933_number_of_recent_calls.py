class RecentCounter:

    def __init__(self):
        self.__calls: list[int] = []

    def ping(self, xt: int) -> int:
        while len(self.__calls) != 0 and xt - self.__calls[0] > 3000:
            self.__calls.pop(0)
        self.__calls.append(xt)
        return len(self.__calls)


rc = RecentCounter()
print([rc.ping(e) for e in [1, 100, 3001, 3002]])
