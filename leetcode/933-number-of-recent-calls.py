class RecentCounter:

    def __init__(self):
        self.queuer = []
        self.cnt = 0

    def ping(self, t: int) -> int:
        self.queuer.insert(0, t)
        while self.queuer[0] - self.queuer[-1] > 3000:
            self.queuer.pop()
        return len(self.queuer)