function invertBinaryTree(tree) {
	// Write your code here.
	const dfs = (node) => {
		if (node == null) {
			return null;
		}
		const temp = node.left;
		node.left = dfs(node.right);
		node.right = dfs(temp);
		return node;
	};

	return dfs(tree);
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
exports.invertBinaryTree = invertBinaryTree;
