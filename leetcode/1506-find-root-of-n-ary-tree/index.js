/*
    1st: bfs?
    - check the indgree of each node

    Time    O(N)
    Space   O(N)
    192 ms, faster than 57.14%
*/
var findRoot = function (nodes) {
	const ht = new Map();
	for (let node of nodes) {
		if (ht.get(node) === undefined) {
			ht.set(node, 0);
		}
		for (let child of node.children) {
			if (child in ht) {
				ht.set(child, ht.get(child) + 1);
			} else {
				ht.set(child, 1);
			}
		}
	}
	for (let [key, val] of ht) {
		if (val == 0) {
			return key;
		}
	}
	return null;
};
