#341. Flatten Nested List Iterator
"""
Time Compelxity : O(no of integers + no of lists)
Space Complexity : O(no of integers + recursive stack)
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nestedList):
            for i in nestedList:
                if i.isInteger():
                    self.integers.append(i.getInteger())
                else:
                    flatten(i.getList())
        self.integers = []
        self.pos = -1
        flatten(nestedList)
        
    def next(self) -> int:
        #O(1) - Time complexity
        self.pos += 1
        return self.integers[self.pos]


    def hasNext(self) -> bool:
        #O(1) - Time complexity
        return self.pos + 1 < len(self.integers)
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
