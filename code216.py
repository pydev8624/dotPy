class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f"Called {self.count} time(s).")

c = Counter()


c()   # Called 1 time(s)
c()   # Called 2 time(s)
c()   # Called 3 time(s)
