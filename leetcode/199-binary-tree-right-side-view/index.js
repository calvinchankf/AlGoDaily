/*
    1st approach: bfs
    - declare a result array
    - when we traverse down, put the val into the result if the depth > len(array)

    Time    O(n)
    Space   O(h)
    104 ms, faster than 17.31%
*/
var rightSideView = function (root) {
	if (!root) {
		return [];
	}
	const res = [];
	const q = [[root, 1]];
	while (q.length > 0) {
		const [node, depth] = q.shift();

		if (depth > res.length) {
			res.push(node.val);
		}

		if (node.right) {
			q.push([node.right, depth + 1]);
		}
		if (node.left) {
			q.push([node.left, depth + 1]);
		}
	}
	return res;
};
