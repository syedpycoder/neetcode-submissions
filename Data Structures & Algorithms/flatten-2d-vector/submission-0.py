class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.flat_list = []
        self.currentPos = 0

        for innerList in self.vec:
            for num in innerList:
                self.flat_list.append(num)

    def next(self) -> int:
        value = self.flat_list[self.currentPos]
        self.currentPos += 1
        return value
    def hasNext(self) -> bool:
        return self.currentPos < len(self.flat_list)
