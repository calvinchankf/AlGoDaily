/*
    1st: recusive dfs

    Time    O(N)
    Space   O(h)
    68 ms, faster than 54.89%
*/
var invertTree = function (root) {
	if (root == null) {
		return null;
	}
	const temp = root.left;
	root.left = invertTree(root.right);
	root.right = invertTree(temp);
	return root;
};

var invertTree = function (root) {
	if (root == null) {
		return null;
	}
	[root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
	return root;
};

/*
    2nd: BFS

    Time    O(N)
    Space   O(h)
    68 ms, faster than 54.89%
*/
var invertTree = function (root) {
	if (root == null) {
		return null;
	}
	const q = [root];
	while (q.length > 0) {
		const node = q.shift();
		[node.left, node.right] = [node.right, node.left];
		if (node.left !== null) {
			q.push(node.left);
		}
		if (node.right !== null) {
			q.push(node.right);
		}
	}
	return root;
};
