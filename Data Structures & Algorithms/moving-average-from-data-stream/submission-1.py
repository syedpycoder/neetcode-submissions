class MovingAverage:

    def __init__(self, size: int):
        self.element_arr = []
        self.size = size        

    def next(self, val: int) -> float:
        self.element_arr.append(val)
        if len(self.element_arr) <= self.size:
            moving_sum = sum(self.element_arr)
            current_len = len(self.element_arr)
            moving_avg = moving_sum / current_len
            return moving_avg
        else:
            moving_sum = sum(self.element_arr[(len(self.element_arr) - self.size):])  
            return moving_sum / self.size  
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
