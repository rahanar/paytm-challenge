from abc import ABC, abstractmethod

class MovingAverageInterface(ABC):
    """
    This interface defines all methods that are
    required to be implemented to calculate
    moving average of N elements.
    """

    @abstractmethod
    def getMovingAverage(self) -> float:
        """
        Return a moving average of N elements.
        """
        pass

    @abstractmethod
    def addElement(self, element: int):
        """
        Add an element to the queue and calculate new
        average of elements in the queue.
        """
        pass

    @abstractmethod
    def getElements(self) -> list:
        """
        Return all elements that are currently in the
        queue as a list.
        """
        pass
