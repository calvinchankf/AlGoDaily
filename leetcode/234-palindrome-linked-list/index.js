/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */


/*
    1st: brute force
	- just put the items into an array and check
	Time		O(2N)
	Space       O(N)
	84 ms, faster than 67.58%
*/
var isPalindrome = function(head) {
    const arr = []
    let cur = head
    while (cur != null) {
        arr.push(cur.val)
        cur = cur.next
    }
    let i = 0
    let j = arr.length - 1
    while (i <= j) {
        if (arr[i] != arr[j]) {
            return false
        }
        i += 1
        j -= 1
    }
    return true
};

/*
    2nd approach: 2 pointers
    - slow walks 1 step at a time, fast walks 2 steps at a time
    - slow stops at the node points to the 2nd half
    - reverse the 2nd half
    - traverse the 1st half and the 2nd half to see if the values equal

    Time    O(2n)
    Space   O(1)
    72 ms, faster than 93.58%
*/
var isPalindrome = function(head) {
    let slow = head
    let fast = head
    while (fast != null && fast.next != null) {
        slow = slow.next
        fast = fast.next.next
    }
    const head2 = reverseList(slow)
    
    let cur1 = head
    let cur2 = head2
    while (cur1 && cur2) {
        if (cur1.val != cur2.val) {
            return false
        }
        cur1 = cur1.next
        cur2 = cur2.next
    }
    return true
};

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