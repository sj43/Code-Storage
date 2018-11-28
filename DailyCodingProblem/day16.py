class Log(object):
    def __init__(self, n):
        self._log = []
        self.n = n
        self.current = 0

    def record(self, order_id):
        if len(self._log) == self.n:
            self._log[self.current] = order_id
        else:
            self._log.append(order_id)
        self.current = (self.current + 1) % self.n

    def get_last(self, i):
        return self._log[self.current-i]
 
