/*
    2nd: BFS + hashtable
    - but this time we change the word to get the next combination instead of finding it from the wordList,
    because there might be a lot of words in the wordList which just have 1 digit difference

    Time    O(n^26*wordLength) for each word, traverse the similar words
    Space   O(n)
    1488 ms, faster than 13.34%
*/
var ladderLength = function (beginWord, endWord, wordList) {
	const wordSet = new Set(wordList);
	if (!wordSet.has(endWord)) {
		return 0;
	}
	const visited = new Set();
	const q = [[beginWord, 1]];
	const cands = "abcdefghijklmnopqrstuvwxyz";
	while (q.length > 0) {
		const [node, steps] = q.shift();
		if (node == endWord) {
			return steps;
		}
		if (visited.has(node)) {
			continue;
		}
		visited.add(node);
		for (let i = 0; i < node.length; i++) {
			for (let c of cands) {
				const temp = node.slice(0, i) + c + node.slice(i + 1);
				if (wordSet.has(temp)) {
					q.push([temp, steps + 1]);
				}
			}
		}
	}
	return 0;
};

/*
    3rd: bi directional BFS + hashtable
    - but this time we change the word to get the next combination instead of finding it from the wordList,
    because there might be a lot of words in the wordList which just have 1 digit difference

    Time    O(n^26*wordLength) for each word, traverse the similar words
    Space   O(n)
    1172 ms, faster than 16.64%
*/
var ladderLength = function (beginWord, endWord, wordList) {
	const wordSet = new Set(wordList);
	if (!wordSet.has(endWord)) {
		return 0;
	}

	const cands = "abcdefghijklmnopqrstuvwxyz";

	const visited1 = {};
	const q1 = [[beginWord, 1]];

	const visited2 = {};
	const q2 = [[endWord, 0]];

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
						if (wordSet.has(temp)) {
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
						if (wordSet.has(temp)) {
							q2.push([temp, steps + 1]);
						}
					}
				}
			}
		}
	}
	return 0;
};
