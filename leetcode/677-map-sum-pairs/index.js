/*
    1st: trie
    - use dfs to sum up all the node.count

    Time of insert()   O(N)
    Time of insert()   O(N)
    Space   O(N)
    128 ms, faster than 7.50%
*/
class Node {
	constructor() {
		this.children = {};
		this.count = 0;
	}
}

var MapSum = function () {
	this.root = new Node();
};

MapSum.prototype.insert = function (key, val) {
	let cur = this.root;
	for (let c of key) {
		if (cur.children[c] === undefined) {
			cur.children[c] = new Node();
		}
		cur = cur.children[c];
	}
	cur.count = val;
};

MapSum.prototype.sum = function (prefix) {
	let cur = this.root;
	for (let c of prefix) {
		if (cur.children[c] === undefined) {
			return 0;
		}
		cur = cur.children[c];
	}

	let res = 0;
	const dfs = (node) => {
		if (node == null) {
			return;
		}
		res += node.count;
		for (let key in node.children) {
			dfs(node.children[key]);
		}
	};
	dfs(cur);

	return res;
};

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */
