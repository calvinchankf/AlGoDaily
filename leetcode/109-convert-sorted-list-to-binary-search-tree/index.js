/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: build bst with recursion

    Time    O(N)
    Space   O(N)
    96 ms, faster than 56.04%
*/
var sortedListToBST = function (head) {
	const nums = [];
	let cur = head;
	while (cur != null) {
		nums.push(cur.val);
		cur = cur.next;
	}
	return sortedArrayToBST(nums);
};

var sortedArrayToBST = function (nums) {
	if (nums.length == 0) {
		return null;
	}
	const mid = Math.floor(nums.length / 2);
	const node = new TreeNode(nums[mid]);
	node.left = sortedArrayToBST(nums.slice(0, mid));
	node.right = sortedArrayToBST(nums.slice(mid + 1));
	return node;
};

/*
    2nd: optimize the speed by using indices instead of array slicing

    Time    O(2n)
    Space   O(n)
    100 ms, faster than 55.08%
*/
var sortedListToBST = function (head) {
	const nums = [];
	let cur = head;
	while (cur != null) {
		nums.push(cur.val);
		cur = cur.next;
	}
	return sortedArrayToBST(nums, 0, nums.length - 1);
};

var sortedArrayToBST = function (nums, left, right) {
	if (left > right) {
		return null;
	}
	const mid = Math.floor((left + right) / 2);
	const node = new TreeNode(nums[mid]);
	node.left = sortedArrayToBST(nums, left, mid - 1);
	node.right = sortedArrayToBST(nums, mid + 1, right);
	return node;
};
