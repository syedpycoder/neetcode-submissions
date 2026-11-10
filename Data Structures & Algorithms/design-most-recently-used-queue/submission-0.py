class MRUQueue:
    def __init__(self, n: int):
        self.bucket = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        val = self.bucket.pop(k-1)
        self.bucket.append(val)
        return val
