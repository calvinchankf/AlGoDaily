/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/*
    1st approach
    - similar to reverse linked list and reverse halh of a linked list
    - we need to find the parent of node[m] first, reverse the later list until the count < n(right)
    20ms beats 100%

    Time    O(N)
    Space   O(1)
    84 ms, faster than 19.01% 
*/
var reverseBetween = function(head, m, n) {
    
    const dumphead = new ListNode()
    dumphead.next = head
    
    let parent = dumphead 
    let cur = head
    let count = 1
    while (cur != null && count < m) {
        parent = cur
        cur = cur.next
        count += 1
    }
    let newHead = cur
    while (cur != null && cur.next != null && count < n) {
        const temp = cur.next
        cur.next = cur.next.next
        temp.next = newHead
        newHead = temp
        count += 1
    }
    parent.next = newHead
    return dumphead.next
};