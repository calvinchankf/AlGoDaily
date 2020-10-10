/*
    classic approach: bottom-up recursion + memorization
    - similar to lc132
    - see ./idea.png

    ref:
    - https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS

    Time    O(n^2*k) Size of recursion tree can go up to n^2. The creation of list takes k time.
    Space   O(n^2*k)
    76 ms, faster than 96.35%
*/
var wordBreak = function (s, wordDict) {
	const m = {};
	const wordSet = new Set(wordDict);
	return explore(s, wordSet, m);
};

const explore = (s, wordSet, m) => {
	if (s.length === 0) {
		return [""];
	}
	if (s in m) {
		return m[s];
	}
	const res = [];
	for (let w of wordSet) {
		const n = w.length;
		const cand = s.slice(0, n);
		if (w === cand) {
			const suffixArr = explore(s.slice(n), wordSet, m);
			for (let suffix of suffixArr) {
				const newS = w + " " + suffix;
				res.push(newS.trim());
			}
		}
	}
	m[s] = res;
	return m[s];
};
