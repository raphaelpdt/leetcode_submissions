# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0 or lists is None: return None
        if len(lists) == 1: return lists[0]
        
        mid = len(lists) / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left, right) # merge the lists
            
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """    
        if l1 is None: return l2
        if l2 is None: return l1
        
        dummy = ListNode()
        curr = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        # append remainder of any list that is not completely iterated through
        if l1 is not None: curr.next = l1
        elif l2 is not None: curr.next = l2
        
        return dummy.next