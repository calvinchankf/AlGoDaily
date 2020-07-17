/*
    1st: recursive DFS
    - when we traverse the tree, replace each of a child to its clone using the result from the recursive function

    Time    O(N)
    Space   O(N) recursion tree
    Runtime: 80 ms
    Memory Usage: 17.6 MB
*/
var cloneTree = function (root) {
	if (root == null) {
		return null;
	}
	const node = new Node(root.val);
	for (let child of root.children) {
		node.children.push(cloneTree(child));
	}
	return node;
};

/*
    2nd: BFS
    - store node and its parent when we traverse the tree
    - append a clone child to its parent every time we dequeue

    Time    O(N)
    Space   O(N) queue
    Runtime: 80 ms, faster than 100.00%
    Memory Usage: 17.6 MB, less than 100.00%
*/
var cloneTree = function (root) {
	if (root == null) {
		return null;
	}
	let newRoot = null;
	const q = [[null, root]];
	while (q.length > 0) {
		const [parent, head] = q.shift();
		const node = new Node(head.val);
		if (newRoot == null) {
			newRoot = node;
		}
		if (parent !== null) {
			parent.children.push(node);
		}
		for (let child of head.children) {
			q.push([node, child]);
		}
	}
	return newRoot;
};
