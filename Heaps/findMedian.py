import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # first half of the pq
        self.large = [] # second half of the pq

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            # add to large queue
            # NOTE: Python's implementation of heap is a min heap, so we push in
            #  negative numbers to mimic a max heap
            # NOTE: 'heappushpop' pushes the specified val then immediately pops highest priority
            #   entry
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            # add to small queue
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
            
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            # length is even, return median of two mid values
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()