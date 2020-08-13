/*
    1st approach: recursive dfs
    
    Time  O(n)
    Space O(h)
    96 ms, faster than 61.56%
*/
var pathSum = function (root, sum) {
	let res = [];
	const dfs = (node, arr, total) => {
		if (node == null) {
			return;
		}
		const newArr = [...arr, node.val];
		const newTotal = total + node.val;
		if (node.left == null && node.right == null && newTotal == sum) {
			res.push(newArr);
		}
		dfs(node.left, newArr, newTotal);
		dfs(node.right, newArr, newTotal);
	};
	dfs(root, [], 0);

	return res;
};
