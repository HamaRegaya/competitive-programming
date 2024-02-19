class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None]*n
        self.pointer = 0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        idKey-=1
        self.stream[idKey] = value
        if self.pointer >= idKey:
            while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
                self.pointer+=1
            return self.stream[idKey:self.pointer]
        else:
            return []
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)