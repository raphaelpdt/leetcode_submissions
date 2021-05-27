/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution
{
    // First solution, using a two pointer approach
    public ListNode RemoveNthFromEnd(ListNode head, int n)
    {
        if (head == null)
            return head;

        if (head.next == null && n == 1)
            return null;

        // Two pointers, fast is to maintain end of list pos
        // slow is to traverse to "nth" node
        ListNode slow = head;
        ListNode fast = head;

        // Position fast pointer n pos ahead of slow
        while (n != 0)
        {
            fast = fast.next;
            n -= 1;
        }

        // EDGE CASE: remove the first entry only
        if (fast == null)
            return head.next;

        // Iterate nodes such that at the end of this loop,
        // fast will be pointing to the final node of the LL, and 
        // slow will be pointing to before the "nth" node from end
        while (fast.next != null)
        {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return head;
    }

    // Re-attempt, using a counter to track the target
    public ListNode removeNthFromEnd_v2 (ListNode head)
    {
        if (head == null)
            return head;

        if (head.next == null && n == 1)
            return null;

        int LL_len = 0; // keep a counter for LL length
        ListNode curr = head; // keep head pointed to start of list, so use a copy
        while (curr != null)
        {
            LL_len++;
            curr = curr.next;
        }

        LL_len--; // decrement by 1 to account for 0-based indexing

        // EDGE CASE: adjusted len counter is less than n must mean we only
        // need to remove the first entry
        if (LL_len < n)
            return head.next;

        int targetIndex = LL_len - n;
        curr = head; // reset curr pos
        for (int i = 0; i < targetIndex; i++)
        {
            curr = curr.next;
        }

        curr.next = curr.next.next; // have the pointer skip over target node, thus, deleting from LL
        return head;
    }
}