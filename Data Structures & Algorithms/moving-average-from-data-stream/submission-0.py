class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.bucket = []
        

    def next(self, val: int) -> float:
        self.bucket.append(val)
        n = len(self.bucket)
        if n < self.size:
            moving_sum = sum(self.bucket)
            avg = moving_sum / n
        else:
            moving_sum = sum(self.bucket[n-self.size:])
            avg = moving_sum/self.size
        return avg         
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
