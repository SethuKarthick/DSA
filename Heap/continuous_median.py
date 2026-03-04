import heapq

numbers = [5, 10, 100, 200, 6, 13]


class ContinuousMedian:
    def __init__(self):
        self.low = []
        self.high = []
        self.median = None

    def insert(self, num):

        if not len(self.low) or num < self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)

        if len(self.low) - len(self.high) > 1:
            value = heapq.heappop(self.low)
            heapq.heappush(self.high, -value)
        elif len(self.high) - len(self.low) > 1:
            value = heapq.heappop(self.high)
            heapq.heappush(self.low, -value)

        self.update_median()

    def update_median(self):

        if len(self.low) == len(self.high):
            if not len(self.low):
                self.median = None
            else:
                self.median = (-self.low[0] + self.high[0]) / 2
        elif len(self.low) > len(self.high):
            self.median = -self.low[0]
        else:
            self.median = self.high[0]

    def get_median(self):
        return self.median

if __name__ == "__main__":
    handler = ContinuousMedian()
    for num in numbers:
        handler.insert(num)

    print(handler.get_median())

