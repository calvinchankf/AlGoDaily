/*
    1st: minimum spanning tree (kruskal: union find + sort)

    Time		O(E log E) + O(V log V) <= sort the edges + union find
	Space		O(V) edges in union find
      
    E: number of edges
    V: number of vertices
    
     116 ms, faster than 94.34%
*/

var minimumCost = function (N, connections) {
	const uf = new UnionFind(N);
	connections.sort((a, b) => {
		return a[2] - b[2];
	});
	let res = 0;
	for (let [a, b, c] of connections) {
		rootA = uf.find(a);
		rootB = uf.find(b);
		if (rootA != rootB) {
			uf.union(a, b);
			res += c;
		}
	}
	if (uf.count > 1) {
		return -1;
	}
	return res;
};

class UnionFind {
	constructor(N) {
		this.count = N;
		this.roots = {};
		this.caps = {};
		for (let i = 1; i < N + 1; i++) {
			this.roots[i] = i;
			this.caps[i] = 1;
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
		this.count -= 1;
	};
}

let a = 3;
let b = [
	[1, 2, 5],
	[1, 3, 6],
	[2, 3, 1],
];
console.log(minimumCost(a, b));

a = 4;
b = [
	[1, 2, 3],
	[3, 4, 4],
];
console.log(minimumCost(a, b));

console.log("-----");

/*
    2nd: minimum spanning tree (prim)

	Time	O(E log V) E: number of edges, V: number of vertices
	Space	O(E + V) hashtable + heap

	ref:
	- https://www.youtube.com/watch?v=YyLaRffCdk4
*/
var minimumCost = function (N, connections) {
	const graph = {};
	for (let [a, b, cost] of connections) {
		if (graph[a] === undefined) {
			graph[a] = [[cost, b]];
		} else {
			graph[a].push([cost, b]);
		}
		if (graph[b] === undefined) {
			graph[b] = [[cost, a]];
		} else {
			graph[b].push([cost, a]);
		}
	}
	console.log(graph);
	const q = [[0, 1]];
	const visited = new Set();
	let total = 0;
	while (q.length > 0 && visited.size < N) {
		const [cost, node] = q.shift();
		if (visited.has(node)) {
			continue;
		}
		visited.add(node);
		total += cost;
		if (graph[node] === undefined) {
			continue;
		}
		for (let [edge_cost, next_node] of graph[node]) {
			const indexToInsert = upperBsearch(q, edge_cost);
			q.splice(indexToInsert, 0, [edge_cost, next_node]);
		}
	}
	return visited.size == N ? total : -1;
};

const upperBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target >= nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};

let a = 3;
let b = [
	[1, 2, 5],
	[1, 3, 6],
	[2, 3, 1],
];
console.log(minimumCost(a, b));

a = 4;
b = [
	[1, 2, 3],
	[3, 4, 4],
];
console.log(minimumCost(a, b));

a = 5;
b = [
	[2, 1, 3267],
	[3, 2, 25910],
	[4, 1, 30518],
];
console.log(minimumCost(a, b));
