// This is the class of the input root.
// Do not edit it.
class BinaryTree {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

/*
    DFS
    Time    O(N)
    Space   O(H)
*/
function branchSums(root) {
	// Write your code here.
	const res = [];

	const dfs = (node, sum) => {
		if (node === null) {
			return;
		}
		const newSum = sum + node.value;
		if (node.left === null && node.right === null) {
			res.push(newSum);
			return;
		}
		dfs(node.left, newSum);
		dfs(node.right, newSum);
	};
	dfs(root, 0);

	return res;
}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.branchSums = branchSums;
