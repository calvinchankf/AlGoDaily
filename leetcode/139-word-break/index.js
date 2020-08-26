/*
    1st approach: recursion + memorization
    - e.g. "catsandogab", ["cats", "dog", "sand", "and", "cat", "og", "ab"]
        from the begining, we can split it into 2 strings
        [cat,sandogab], [cats, andogab]
        then they can become in the next recursion
        [cat,sand,ogab], [cat,sand,ogab]
        then 
        [cat,sand,og,ab], [cat,sand,og,ab]
    - actually we did [cat,sand,ogab], we know that "ogab" is breakable after the recursion,
        therefore we can save "ogab" as "true" so that we can avoid redundant computation if we meet "ogab" again

    Time    O(n^2)
    Space   O(n)

    88 ms, faster than 39.98%
*/
var wordBreak = function (s, wordDict) {
	const m = {};
	const wordSet = new Set(wordDict);
	return explore(s, wordSet, m);
};

const explore = (s, wordSet, m) => {
	if (s.length === 0) {
		return true;
	}
	if (s in m) {
		return m[s];
	}
	for (let w of wordSet) {
		const n = w.length;
		const cand = s.slice(0, n);
		if (w === cand) {
			const isFound = explore(s.slice(n), wordSet, m);
			if (isFound) {
				m[s] = true;
				return true;
			}
		}
	}
	m[s] = false;
	return false;
};
