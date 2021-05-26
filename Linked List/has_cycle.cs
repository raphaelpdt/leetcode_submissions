/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public bool HasCycle(ListNode head) {
        // BASE CASE: empty list or list only has one node
        if (head == null || head.next == null)
            return false;
        
        // build a set to record nodes that have been visited
        HashSet<ListNode> visited = new HashSet<ListNode>();
        ListNode curr = head;
        while (curr != null)
        {
            if (visited.Contains(curr))
            {
                return true;
            }
            
            visited.Add(curr);
            curr = curr.next;
        }
        
        // if while loop terminates, there is no cycle
        return false;
    }

    // Alt. implementation with two-ptr approach for O(1) space
    public bool HasCycle_o1_space(ListNode head)
    {
        // BASE CASE: empty list or list only has one node
        if (head == null || head.next == null)
            return false;

        // set a fast pointer and slow pointer to traverse the list
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && slow != null)
        {
            if (fast == slow)
            {
                return true;
            }

            // jump to two nodes over, however,
            // do not access "next-next" pointer if next is null
            fast = fast.next?.next;
            slow = slow.next; // increment to next node
        }

        // if while loop terminates, there is no cycle
        return false;
    }
}