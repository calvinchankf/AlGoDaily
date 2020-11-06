/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
/*
    2nd approach: inplace replacement(learned from others)

    idea:
	1->2->3->4
    2->1->3->4
    3->2->1->4
    4->3->2->1

    ref:
    - https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1204/
    
	Time		O(n)
    Space 	    O(1) since in-place
    80 ms, faster than 75.61%
*/
var reverseList = function (head) {
    let newHead = head
    while (head != null && head.next != null) {
        const temp = head.next
        head.next = head.next.next
        temp.next = newHead
        newHead = temp
    }
    return newHead
};