/*
    Status: Wrong Answer
    37 / 39 test cases passed.
*/
var findLadders = function (beginWord, endWord, wordList) {
	const wordSet = new Set(wordList);
	if (!wordSet.has(endWord)) {
		return [];
	}

	const cands = "abcdefghijklmnopqrstuvwxyz";

	const visited1 = {};
	const q1 = [[beginWord, [beginWord]]];

	const visited2 = {};
	const q2 = [[endWord, [endWord]]];

	let res = [];

	let minStepsFromQ1 = Number.MAX_SAFE_INTEGER;
	let minStepsFromQ2 = Number.MAX_SAFE_INTEGER;

	while (q1.length > 0 || q2.length > 0) {
		if (q1.length > 0) {
			const n = q1.length;
			for (let i = 0; i < n; i++) {
				const [node, path] = q1.shift();

				if (node in visited2) {
					const l = visited2[node].length;
					const x = visited2[node].slice(0, l - 1).reverse();
					const temp = path.concat(x);

					const a = path.length;
					const b = temp.length - a;
					// console.log(a, b)

					if (a + b < minStepsFromQ1 + minStepsFromQ2) {
						res = [temp];
						minStepsFromQ1 = a;
						minStepsFromQ2 = b;
					} else if (a + b == minStepsFromQ1 + minStepsFromQ2) {
						res.push(temp);
					}
				}

				// if (path.length >= minStepsFromQ1) {
				//     continue
				// }

				if (node in visited1) {
					continue;
				}
				visited1[node] = path;
				for (let j = 0; j < node.length; j++) {
					for (let c of cands) {
						const temp = node.slice(0, j) + c + node.slice(j + 1);
						if (wordSet.has(temp)) {
							q1.push([temp, [...path, temp]]);
						}
					}
				}
			}
		}

		if (q2.length > 0) {
			const n = q2.length;
			for (let i = 0; i < n; i++) {
				const [node, path] = q2.shift();
				if (node in visited1) {
					// const temp = path.concat(visited1[node])
					const l = path.length;
					const x = path.slice(0, l - 1).reverse();
					const temp = visited1[node].concat(x);

					const a = visited1[node].length;
					const b = temp.length - a;
					// console.log(a, b)

					if (a + b < minStepsFromQ1 + minStepsFromQ2) {
						res = [temp];
						minStepsFromQ1 = a;
						minStepsFromQ2 = b;
					} else if (a + b == minStepsFromQ1 + minStepsFromQ2) {
						res.push(temp);
					}
				}

				// if (path.length >= minStepsFromQ2) {
				//     continue
				// }

				if (node in visited2) {
					continue;
				}
				visited2[node] = path;
				for (let j = 0; j < node.length; j++) {
					for (let c of cands) {
						const temp = node.slice(0, j) + c + node.slice(j + 1);
						if (wordSet.has(temp)) {
							q2.push([temp, [...path, temp]]);
						}
					}
				}
			}
		}
	}

	const ht = {};
	for (let arr of res) {
		const key = arr.join(",");
		ht[key] = arr;
	}

	const final = [];
	for (let key in ht) {
		final.push(ht[key]);
	}

	return final;
};
