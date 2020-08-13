/*
    1st approach: BFS + hashset to avoid loop
    - similar to leetcode 127) word ladder

    Time    O(M×N)  
        M=length of gene, in this case is 8
        N=number of genes in the bank
        Finding out all the transformations takes M iterations for each of the N genes. 
        Also, breadth first search in the worst case might go to each of the N gene.
    Space   O(n)
    64 ms, faster than 91.78%
*/
var minMutation = function (start, end, bank) {
	const bankSet = new Set(bank);
	if (!bankSet.has(end)) {
		return -1;
	}
	const visited = new Set();
	const q = [[start, 0]];
	const cands = ["A", "C", "G", "T"];
	while (q.length > 0) {
		const [node, steps] = q.shift();
		if (node == end) {
			return steps;
		}
		if (visited.has(node)) {
			continue;
		}
		visited.add(node);
		for (let i = 0; i < node.length; i++) {
			for (let c of cands) {
				const temp = node.slice(0, i) + c + node.slice(i + 1);
				if (bankSet.has(temp)) {
					q.push([temp, steps + 1]);
				}
			}
		}
	}
	return -1;
};

/*
    2nd: Bidirectional BFS
    - similar to leetcode 127) word ladder

    Time    O(M×N)  
        M=length of gene, in this case is 8
        N=number of genes in the bank
        Finding out all the transformations takes M iterations for each of the N genes. 
        Also, breadth first search in the worst case might go to each of the N gene.
    Space   O(n)
    72 ms, faster than 57.53%
*/
var minMutation = function (start, end, bank) {
	const bankSet = new Set(bank);
	if (!bankSet.has(end)) {
		return -1;
	}
	const cands = ["A", "C", "G", "T"];

	const visited1 = {};
	const q1 = [[start, 0]];

	const visited2 = {};
	const q2 = [[end, 0]];

	while (q1.length > 0 || q2.length > 0) {
		if (q1.length > 0) {
			const n = q1.length;
			for (let i = 0; i < n; i++) {
				const [node, steps] = q1.shift();
				if (node in visited2) {
					return steps + visited2[node];
				}
				if (node in visited1) {
					continue;
				}
				visited1[node] = steps;
				for (let j = 0; j < node.length; j++) {
					for (let c of cands) {
						const temp = node.slice(0, j) + c + node.slice(j + 1);
						if (bankSet.has(temp)) {
							q1.push([temp, steps + 1]);
						}
					}
				}
			}
		}

		if (q2.length > 0) {
			const n = q2.length;
			for (let i = 0; i < n; i++) {
				const [node, steps] = q2.shift();
				if (node in visited1) {
					return steps + visited1[node];
				}
				if (node in visited2) {
					continue;
				}
				visited2[node] = steps;
				for (let j = 0; j < node.length; j++) {
					for (let c of cands) {
						const temp = node.slice(0, j) + c + node.slice(j + 1);
						if (bankSet.has(temp)) {
							q2.push([temp, steps + 1]);
						}
					}
				}
			}
		}
	}
	return -1;
};
