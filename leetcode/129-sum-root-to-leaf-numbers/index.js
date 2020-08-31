/*
    1st approach
    - recursive dfs + prefix sum
    
	Time	O(N)
	Space	O(h) callstack
	76 ms, faster than 29.65%
*/
var sumNumbers = function (root) {
	let total = 0;

	const dfs = (node, sum) => {
		if (node == null) {
			return;
		}
		const newSum = `${sum}${node.val}`;
		if (node.left == null && node.right == null) {
			total += parseInt(newSum);
			return;
		}
		dfs(node.left, newSum);
		dfs(node.right, newSum);
	};
	dfs(root, "");

	return total;
};

/*
    2nd: or use number
    - recursive dfs + prefix sum
    
	Time	O(N)
	Space	O(h) callstack
	76 ms, faster than 29.65%
*/
var sumNumbers = function (root) {
	let total = 0;

	const dfs = (node, sum) => {
		if (node == null) {
			return;
		}
		const newSum = sum * 10 + node.val;
		if (node.left == null && node.right == null) {
			total += newSum;
			return;
		}
		dfs(node.left, newSum);
		dfs(node.right, newSum);
	};
	dfs(root, 0);

	return total;
};
