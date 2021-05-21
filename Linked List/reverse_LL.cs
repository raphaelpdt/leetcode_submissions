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
    public ListNode ReverseList(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        ListNode prev = null;
        ListNode curr = head;
        while (curr != null)
        {
            // temporarily store next node then make current node point
            // to preceding node
            ListNode temp = curr.next;
            curr.next = prev;

            // iterate prev pointer to point to curr entry and next
            // ptr to point to next node in the list
            prev = curr;
            curr = temp;
        }

        // prev will now be pointing at the new head
        return prev;
    }
}

// The following link has a great gif to viz this problem: https://www.geeksforgeeks.org/reverse-a-linked-list/