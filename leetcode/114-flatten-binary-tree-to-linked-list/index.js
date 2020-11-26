/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/*
    1st approach: 
    - similar to lc114, 426, 430
    - store the nodes' values
    - add the values back to the linked list

    Time    O(2N)
    Space   O(N)
    84 ms, faster than 66.78%
*/
var flatten = function (root) {
	if (root == null) {
		return;
	}

	const arr = [];
	const preorder = (node) => {
		if (node == null) {
			return;
		}
		arr.push(node);
		preorder(node.left);
		preorder(node.right);
	};
	preorder(root);

	let prev = root;
	for (let i = 1; i < arr.length; i++) {
		const x = arr[i];
		prev.left = null;
		prev.right = x;
		prev = x;
	}
	prev.left = null;
	prev.right;
};

/*
    2nd approach: recursion
    - similar to lc114, 426, 430
    - store the nodes' values
    - add the values back to the linked list

    Time    O(N)
    Space   O(N)
    104 ms, faster than 10.91% 
*/
var flatten = function(root) {
    if (root == null) {
        return
    }
    let dumphead = new TreeNode(root)
    let prev = dumphead
    const preorder = (node) => {
        if (node === null) {
            return
        }
        const rightChild = node.right
        prev.left = null
        prev.right = node
        prev = node
        preorder(node.left)
        preorder(rightChild)
    }
    preorder(root)
    return dumphead.right
};