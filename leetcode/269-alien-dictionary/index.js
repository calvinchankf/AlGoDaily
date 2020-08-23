/*
    1st approach: topological ordering in bfs using queue
    1. construct the edges
    2. topo sort

    weird corner cases:
    1. ['abc', 'ab'] return ''
    1. ['ab', 'abc'] return 'abc'
    1. ['z','z'] return 'z'

    Time    O(V+E)
    Space   O(V)
    92 ms, faster than 58.68% 
*/
var alienOrder = function (words) {
	const wordSet = new Set(words);
	if (wordSet.size == 1) {
		return words[0];
	}

	const nodeSet = new Set();
	const edges = []; // [[from, to]]:  [w,e], [t,f]...etc

	// words = Array.from(wordSet)
	for (let i = 0; i < words.length; i++) {
		for (let j = 0; j < words[i].length; j++) {
			nodeSet.add(words[i][j]);
		}
	}

	for (let i = 1; i < words.length; i++) {
		const prevWord = words[i - 1];
		const word = words[i];
		let j = 0;
		for (; j < Math.min(prevWord.length, word.length); j++) {
			if (prevWord[j] !== word[j]) {
				edges.push([prevWord[j], word[j]]);
				break;
			}
		}
		// corner case: [abc, ab], return ''
		if (prevWord.indexOf(word) == 0 && prevWord.length > word.length) {
			return "";
		}
	}

	// console.log(edges)

	const indegees = {};
	const collections = {};

	for (let c of nodeSet.keys()) {
		indegees[c] = 0;
		collections[c] = [];
	}

	for (let [f, t] of edges) {
		indegees[t] += 1;
		collections[f].push(t);
	}

	// console.log(indegees)
	// console.log(collections)

	const q = [];
	for (let key in indegees) {
		if (indegees[key] == 0) {
			q.push(key);
		}
	}

	// console.log(q)

	if (q.length == nodeSet.size) {
		return Array.from(nodeSet.keys()).join("");
	}

	let res = "";
	while (q.length > 0) {
		const node = q.shift();
		res += node;
		if (node in collections) {
			for (let child of collections[node]) {
				indegees[child] -= 1;
				if (indegees[child] == 0) {
					q.push(child);
				}
			}
		}
	}

	if (res.length != nodeSet.size) {
		return "";
	}
	return res;
};
