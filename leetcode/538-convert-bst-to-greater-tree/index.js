/*
    1st approach: recursive dfs
    - sorted list is the inorder traversal of the BST
    - use suffixSum to calculate the target values
    - update the nodes' value with the suffixSums

    Time    O(3n)
    Space   O(n)
    72 ms, faster than 32.67%
*/
var convertBST = function (root) {
	const nums = [];
	const inorder = (node) => {
		if (node == null) {
			return;
		}
		inorder(node.left);
		nums.push(node.val);
		inorder(node.right);
	};
	inorder(root);

	let sfs = 0;
	const sfsMap = {};
	for (let i = nums.length - 1; i >= 0; i--) {
		sfs += nums[i];
		sfsMap[nums[i]] = sfs;
	}

	const addSfs = (node) => {
		if (node == null) {
			return;
		}
		node.val = sfsMap[node.val];
		addSfs(node.left);
		addSfs(node.right);
	};
	addSfs(root);

	return root;
};
