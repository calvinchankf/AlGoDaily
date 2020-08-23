/*
    1st approach: bfs + hashtable + sort
    - similar to lc314

    Time    O(n)
    Space   O(n)
    80 ms, faster than 66.27%
*/
var verticalTraversal = function (root) {
	if (root === null || root === undefined) {
		return [];
	}
	const ht = {};
	const q = [[root, 0, 0]]; // node, row, col
	while (q.length > 0) {
		const [node, row, col] = q.shift();
		if (col in ht) {
			ht[col].push([row, node.val]);
		} else {
			ht[col] = [[row, node.val]];
		}
		if (node.left) {
			q.push([node.left, row + 1, col - 1]);
		}
		if (node.right) {
			q.push([node.right, row + 1, col + 1]);
		}
	}

	const keys = Object.keys(ht);
	keys.sort((a, b) => parseInt(a) - parseInt(b));

	const res = [];
	for (let key of keys) {
		const arr = ht[key].sort((a, b) => {
			if (a[0] === b[0]) {
				return a[1] - b[1];
			}
			return a[0] - b[0];
		});
		const temp = [];
		for (let x of arr) {
			temp.push(x[1]);
		}
		res.push(temp);
	}

	return res;
};
