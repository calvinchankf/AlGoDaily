class UnionFind {
	constructor(N) {
		this.count = N;
		this.roots = {};
		this.caps = {};
		for (let i = 0; i < N; i++) {
			this.roots[i] = i;
			this.caps[i] = 1;
		}
	}
	find = (key) => {
		// loop to find to the ultimate root
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
		// e.g. if size of group of pId < size of group of qId, set root of pId to qId
		if (this.caps[pId] < this.caps[qId]) {
			this.roots[pId] = qId;
			this.caps[qId] += this.caps[pId];
		} else {
			this.roots[qId] = pId;
			this.caps[pId] += this.caps[qId];
		}
		this.count -= 1;
	};
}

const N = 5;
const uf = new UnionFind(N);

uf.union(0, 1);

uf.union(2, 3);
uf.union(3, 4);

const ht = {};
for (let i = 0; i < N; i++) {
	const root = uf.find(i);
	if (root in ht) {
		ht[root].push(i);
	} else {
		ht[root] = [i];
	}
}
console.log(ht);

let largestGroup = [];
for (let key in ht) {
	if (ht[key].length > largestGroup.length) {
		largestGroup = ht[key];
	}
}
console.log(largestGroup);
