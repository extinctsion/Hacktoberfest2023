//Best Approach: Two pointers - slow & fast (Floyd's Cycle-Finding Algorithm)
//Employs 2 pointers moving at different speeds. If there is a cycle, the fast pointer will eventually catch up to the slow pointer, confirming cycle.

public boolean hasCycle(ListNode head) 
{
    ListNode slow=head;
    ListNode fast=head;
    while(fast!=null && fast.next!=null)
    {
        slow=slow.next;
        fast=fast.next.next;
        if(slow==fast && slow!=null)
        return true;
    }
    return false;
}
