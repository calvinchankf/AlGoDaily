/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/*
    1st: DFS
    - use the return of each recursion

    Time    O(N)
    Space   O(N)
    76 ms, faster than 86.98%
*/
var cloneGraph = function (root) {
	const ht = {};
	return buildClone(root, ht);
};

const buildClone = (node, ht) => {
	if (node == null) {
		return null;
	}
	if (node.val in ht) {
		return ht[node.val];
	}

	const clone = new Node(node.val);
	ht[node.val] = clone;

	for (let nb of node.neighbors) {
		const temp = buildClone(nb, ht);
		clone.neighbors.push(temp);
	}
	return clone;
};
