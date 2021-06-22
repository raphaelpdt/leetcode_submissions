# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """    
        dummy = ListNode()
        curr = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                curr, l1 = curr.next, l1.next
            else:
                curr.next = ListNode(l2.val)
                curr, l2 = curr.next, l2.next
        
        # append remainder of any list that is not completely iterated through
        if l1 is not None: curr.next = l1
        elif l2 is not None: curr.next = l2
        
        return dummy.next