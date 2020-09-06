/*
    2nd approach: recursion + hashtable (dynamic programming)
    
    This is another way apart from 1st approach:
    - instead of count the variations, here we count the maximum slice we can do until the remaining string becomes empty

    Time    < O(n*2^k) k: average number of characters of words, but since we use hashtable, it must be smaller
    Space   < O(2^k) the recursion tree, but since we use hashtable, it must be smaller
    804 ms, faster than 9.25%
    Sep1 2020
*/
var findAllConcatenatedWordsInADict = function (words) {
	const m = {};
	const wordSet = new Set(words);
	words.sort((a, b) => b.length - a.length);
	const res = [];
	for (let w of words) {
		const count = explore(w, wordSet, m);
		if (count > 1) {
			res.push(w);
		}
	}
	return res;
};

const explore = (s, wordSet, m) => {
	if (s.length === 0) {
		return 0;
	}
	if (s in m) {
		return m[s];
	}
	let maxCount = Number.MIN_SAFE_INTEGER;
	// slice characters instead of iterating the wordSet
	// because there might be so many words here for this question
	for (let i = 0; i < s.length; i++) {
		const cand = s.slice(0, i + 1);
		if (wordSet.has(cand)) {
			const count = explore(s.slice(i + 1), wordSet, m);
			maxCount = Math.max(maxCount, count);
		}
	}
	if (maxCount < 0) {
		maxCount = Number.MIN_SAFE_INTEGER;
	} else {
		maxCount += 1;
	}
	m[s] = maxCount;
	return m[s];
};

let a;

a = ["cat", "catdog", "dog"];
console.log(findAllConcatenatedWordsInADict(a));

a = [
	"cat",
	"cats",
	"catsdogcats",
	"dog",
	"dogcatsdog",
	"hippopotamuses",
	"rat",
	"ratcatdogcat",
];
console.log(findAllConcatenatedWordsInADict(a));

a = [
	"cat",
	"cats",
	"catsdogcats",
	"dog",
	"dogcatsdog",
	"hippopotamuses",
	"rat",
	"ratcatdogcat",
	"hippo",
	"potamuses",
];
console.log(findAllConcatenatedWordsInADict(a));
