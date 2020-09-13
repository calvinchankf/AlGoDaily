/*
    1st: dynamic programming (recursion + hashtable)
    - similar to lc139,140
    - cache only stores the minLength group of palindrome from the end of the string

    e.g. 'noonabbad'
    'd': ['d']
    'ad': ['d', 'a']
    'bad': ['d', 'a', 'b']
    'bbad': ['d', 'a', 'bb']
    'abbad': ['d', 'abba']
    'nabbad': ['d', 'abba', 'n']
    'onabbad': ['d', 'abba', 'n', 'o']
    'oonabbad': ['d', 'abba', 'n', 'oo']
    'noonabbad': ['d', 'abba', 'noon']
    
    The result cache is 'noonabbad': ['d', 'abba', 'noon']
    Hence, the result is 3 - 1 = 2

    Time    O(N^2) in each recursion we check every suffix O(N), and there are N recursions (because every recursion stops when we see a cache)
    Space   O(N) the suffixes cache
    796 ms, faster than 23.33%
*/
var minCut = function (s) {
	const partitions = dfs(s, {});
	return partitions - 1;
};

const dfs = (s, ht) => {
	if (s.length == 0) {
		return 0;
	}
	if (s in ht) {
		return ht[s];
	}
	let minGroupLen = Number.MAX_SAFE_INTEGER;
	let forwardSub = "";
	let backwardSub = "";
	for (let i = 0; i < s.length; i++) {
		// const sub = s.slice(0, i + 1);
		forwardSub += s[i];
		backwardSub = s[i] + backwardSub;
		if (forwardSub == backwardSub) {
			const groupLen = dfs(s.slice(i + 1), ht) + 1;
			if (groupLen < minGroupLen) {
				minGroupLen = groupLen;
			}
		}
	}
	ht[s] = minGroupLen;
	return ht[s];
};

let a;

a = "aab";
console.log(minCut(a));

a = "a";
console.log(minCut(a));

a = "ab";
console.log(minCut(a));

a = "noonabbad";
console.log(minCut(a));

a = "ababababababababababababcbabababababababababababa";
console.log(minCut(a));

a = "cabababcbc";
console.log(minCut(a));

a = "bobnoonabbadnxna";
console.log(minCut(a));

console.log("-----");
