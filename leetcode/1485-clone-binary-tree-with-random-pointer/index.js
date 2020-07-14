/*
    1st: recursive dfs + hashtable
    - put every node in a hashtable
    - when we clone a tree, use the nodes from hashtable

    Time    O(N)
    Space   O(N)
    132 ms, faster than 100.00%
*/
var copyRandomBinaryTree = function (root) {
	const ht = new Map();

	var buildPool = function (node) {
		if (node === null) {
			return;
		}
		const newNode = new NodeCopy(node.val);
		ht.set(node, newNode);

		buildPool(node.left);
		buildPool(node.right);
	};
	buildPool(root);

	var cloneTree = function (node) {
		if (node === null) {
			return null;
		}
		const newNode = ht.get(node);
		if (node.random) {
			newNode.random = ht.get(node.random);
		}
		newNode.left = cloneTree(node.left);
		newNode.right = cloneTree(node.right);
		return newNode;
	};

	return cloneTree(root);
};

/*
    2nd: recursive dfs + hashtable
    - put every node in a hashtable
    - when we clone a tree, use the nodes from hashtable

    Time    O(N)
    Space   O(N)
    132 ms, faster than 100.00%
*/
var copyRandomBinaryTree = function (root) {
	if (root === null || root === undefined) {
		return null;
	}

	const ht = new Map();
	const q = [root];
	while (q.length > 0) {
		const node = q.shift();
		ht.set(node, new NodeCopy(node.val));
		if (node.left) {
			q.push(node.left);
		}
		if (node.right) {
			q.push(node.right);
		}
	}
	return cloneTree(root, ht);
};

var cloneTree = function (node, ht) {
	if (node === null) {
		return null;
	}
	const newNode = ht.get(node);
	if (node.random) {
		newNode.random = ht.get(node.random);
	}
	newNode.left = cloneTree(node.left, ht);
	newNode.right = cloneTree(node.right, ht);
	return newNode;
};
