/*
    Iterative Inorder Traversal of BST
    156 ms, faster than 64.39%
*/
var BSTIterator = function (root) {
	this.stack = [];
	this.pushLeft(root);
};
BSTIterator.prototype.next = function () {
	const cur = this.stack.pop();
	this.pushLeft(cur.right);
	return cur.val;
};
BSTIterator.prototype.hasNext = function () {
	return this.stack.length > 0;
};
BSTIterator.prototype.pushLeft = function (node) {
	let cur = node;
	while (cur != null) {
		this.stack.push(cur);
		cur = cur.left;
	}
};
