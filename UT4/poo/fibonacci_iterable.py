# ******************
# FIBONACCI ITERABLE
# ******************

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.perv_n = 0
        self.target_n = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
      if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        if self.count == 1:
            self.count += 1
            return 1
        if self.count < self.n:
            self.prev_n, self.target_n = self.target_n, self.prev_n + self.target_n
            self.count += 1
            return self.target_n

def run(n):
    return list(Fibonacci(n))
