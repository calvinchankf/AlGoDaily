/**
 * Definition for a binary tree node.
 */
function TreeNode(val) {
	this.val = val;
	this.left = this.right = null;
}

/*
    3rd: very similar to upper bound binary search BUT
    - here is BSTsearch, only record the sucessor when we go left
    - then the sucessor is either your parent OR your left most leaf in right subtree

    see ./idea.jpeg

    Time    O(logn)
    Space   O(h)
    88 ms, faster than 95.57%
*/
var inorderSuccessor = function (root, p) {
	let successor = null;
	let cur = root;
	while (cur !== null) {
		if (p.val < cur.val) {
			successor = cur;
			cur = cur.left;
		} else {
			cur = cur.right;
		}
	}
	return successor;
};

let a = new TreeNode(2);
let b = new TreeNode(1);

ans = inorderSuccessor(a, b);
console.log(ans);
