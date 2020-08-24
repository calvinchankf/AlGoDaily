function maxPathSum(tree) {
	// Write your code here.
	let res = -Number.MAX_SAFE_INTEGER;

	const dfs = (node) => {
		if (node == null) {
			return 0;
		}
		const left = dfs(node.left);
		const right = dfs(node.right);

		const a = left + node.value + right;
		const b = left + node.value;
		const c = node.value + right;
		const d = node.value;

		res = Math.max(res, a, b, c, d);

		return Math.max(left + node.value, right + node.value, node.value);
	};
	dfs(tree);

	return res;
}

// Do not edit the line below.
exports.maxPathSum = maxPathSum;
