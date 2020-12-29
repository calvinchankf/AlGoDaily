/*
    DFS

    Time    O(N)
    Space   O(H)
*/
function nodeDepths(root) {
	// Write your code here.
	let res = 0;

	const dfs = (node, depth) => {
		if (node === null) {
			return;
		}
		res += depth;
		dfs(node.left, depth + 1);
		dfs(node.right, depth + 1);
	};
	dfs(root, 0);

	return res;
}

// This is the class of the input binary tree.
class BinaryTree {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

// Do not edit the line below.
exports.nodeDepths = nodeDepths;
