class MinStack:

    def __init__(self):
        self.data = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minimums or val <= self.minimums[-1]:
            self.minimums.append(val)

    def pop(self) -> None:
        popped = self.data.pop(-1)
        if popped == self.minimums[-1]:
            self.minimums.pop(-1)
        return popped

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
