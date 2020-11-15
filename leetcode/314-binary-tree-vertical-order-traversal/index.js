/*
    2nd approach: bfs + hashtable + sort
    - similar to lc987

    Time    O(NlogN)
    Space   O(h+n) the height of tree(recursion) + the result
    24ms beats 100%
*/
var verticalOrder = function (root) {
	if (root === null || root === undefined) {
		return [];
	}
	const ht = {};
	const q = [[root, 0]]; // node, col
	while (q.length > 0) {
		const [node, col] = q.shift();
		if (col in ht) {
			ht[col].push(node.val);
		} else {
			ht[col] = [node.val];
		}
		if (node.left) {
			q.push([node.left, col - 1]);
		}
		if (node.right) {
			q.push([node.right, col + 1]);
		}
	}

	const keys = Object.keys(ht);
	keys.sort((a, b) => parseInt(a) - parseInt(b));

	const res = [];
	for (let key of keys) {
		res.push(ht[key]);
	}

	return res;
};
