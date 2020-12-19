/*
    2nd approach: linked list
	1. reverse linked list
	2. add one
	3. reverse linked list

	Time		O(3n)
	Space		O(1)
	84 ms, faster than 28.21%
*/
var plusOne = function(head) {
    head = reverse(head)
    let carry = 1
    let cur = head
    while (cur != null && carry > 0) {
        const t = cur.val + carry
        cur.val = t%10
        carry = Math.floor(t/10)
        cur = cur.next
    }
    if (carry > 0) {
        return new ListNode(carry, reverse(head))
    }
    return reverse(head)
};

const reverse = (head) => {
    let newHead = head
    while (head.next != null) {
        const temp = head.next
        head.next = head.next.next
        temp.next = newHead
        newHead = temp
    }
    return newHead
}