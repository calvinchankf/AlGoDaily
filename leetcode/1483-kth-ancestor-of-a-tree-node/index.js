/*
    1st brute force
    - this is not supposed to be solved in this way but it passes the leetcode OJ for js submissions

    Time of init()              O(1)
    Time of getKthAncestor()    O(N)
    4848 ms, faster than 51.19%
*/

/**
 * @param {number} n
 * @param {number[]} parent
 */
var TreeAncestor = function (n, parent) {
	this.parent = parent;
	this.n = n;
};

/**
 * @param {number} node
 * @param {number} k
 * @return {number}
 */
TreeAncestor.prototype.getKthAncestor = function (node, k) {
	if (node >= this.n) {
		return -1;
	}

	while (k > 0) {
		par = this.parent[node];
		if (par == -1) {
			return -1;
		}
		node = par;
		k -= 1;
	}
	return node;
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * var obj = new TreeAncestor(n, parent)
 * var param_1 = obj.getKthAncestor(node,k)
 */
