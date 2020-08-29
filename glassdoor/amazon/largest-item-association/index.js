class UnionFind {
	constructor(nodes) {
		this.roots = {};
		this.caps = {};
		for (let node of nodes) {
			this.roots[node] = node;
			this.caps[node] = 1;
		}
	}
	find = (key) => {
		let cur = key;
		while (cur != this.roots[cur]) {
			cur = this.roots[cur];
		}
		return cur;
	};
	union = (p, q) => {
		const pId = this.find(p);
		const qId = this.find(q);
		if (pId == qId) {
			return;
		}
		if (this.caps[pId] < this.caps[qId]) {
			this.roots[pId] = qId;
			this.caps[qId] += this.caps[pId];
		} else {
			this.roots[qId] = pId;
			this.caps[pId] += this.caps[qId];
		}
	};
}

const largestItemAssociation = (pairs) => {
	const itemSet = new Set();
	for (let [a, b] of pairs) {
		itemSet.add(a);
		itemSet.add(b);
	}

	// union the pairs
	const items = Array.from(itemSet);
	const uf = new UnionFind(items);

	for (let [a, b] of pairs) {
		uf.union(a, b);
	}

	// find the root of each item
	const ht = {};
	for (let item of items) {
		const root = uf.find(item);
		if (root in ht) {
			ht[root].push(item);
		} else {
			ht[root] = [item];
		}
	}
	// find the largest group
	let largestGroup = [];
	for (let key in ht) {
		if (ht[key].length > largestGroup.length) {
			largestGroup = ht[key];
		} else if (ht[key].length == largestGroup.length) {
			const a = ht[key].join(",");
			const b = largestGroup.join(",");
			if (a < b) {
				largestGroup = ht[key];
			}
		}
	}

	return largestGroup.sort();
};

let a;

// a,b | c,d,e
a = [
	["a", "b"],
	["c", "d"],
	["d", "e"],
];
console.log(largestItemAssociation(a));

// 1,2,5 | 3,4
a = [
	["item1", "item2"],
	["item2", "item5"],
	["item3", "item4"],
];
console.log(largestItemAssociation(a));

// 1,2,3 | 4,5,6
a = [
	["item4", "item5"],
	["item5", "item6"],
	["item1", "item2"],
	["item2", "item3"],
];
console.log(largestItemAssociation(a));
