// This is the class of the input root. Do not edit it.
class BinaryTree {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

function flattenBinaryTree(root) {
	if (!root) {
		return root;
	}
	// Write your code here.
	const arr = [];

	const dfs = (node) => {
		if (node == null) {
			return;
		}
		dfs(node.left);
		arr.push(node);
		dfs(node.right);
	};
	dfs(root);

	// console.log(arr)

	const head = arr[0];
	head.left = null;
	head.right = null;

	let cur = head;
	for (let i = 1; i < arr.length; i++) {
		const node = arr[i];
		node.left = cur;
		node.right = null;

		cur.right = node;
		cur = node;
	}

	return head;
}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.flattenBinaryTree = flattenBinaryTree;
