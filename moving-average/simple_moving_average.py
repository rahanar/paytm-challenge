from collections import deque
from moving_average_interface import MovingAverageInterface

class SimpleMovingAverage(MovingAverageInterface):
    """
    This class implements MovingAverageInterface.
    The class implements Simple Moving Average algorithm.

    It uses a queue as an underlying datastructure
    to track N elements.
    """

    def __init__(self, N):
        self.N = N
        self.queue = deque()
        self.movingAvg = 0.0
        self.sum = 0

    def getMovingAverage(self) -> float:
        return self.movingAvg

    def addElement(self, element: int):
        # if the queue is already full, we need pop
        # a leftmost element and calculate sum after
        # the pop
        if len(self.queue) == self.N:
            old_element = self.queue.popleft()
            self.sum -= old_element

        self.queue.append(element)
        self.sum += element
        self.movingAvg = self.sum / self.N

    def getElements(self) -> list:
        return list(self.queue)
