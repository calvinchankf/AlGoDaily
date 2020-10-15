/*
    1st approach: hashtable

    Time    O(m*(n+m)+m)  m: average length of characters, n: length of input array
    Space   O(n)
    88 ms, faster than 75.36% 
*/
var commonChars = function (A) {
	const caches = [];
	for (let w of A) {
		const counts = Array(26).fill(0);
		for (let c of w) {
			const i = c.charCodeAt(0) - "a".charCodeAt(0);
			counts[i] += 1;
		}
		caches.push(counts);
	}
	const alphabets = "abcdefghijklmnopqrstuvwxyz";
	const res = [];
	for (let i = 0; i < 26; i++) {
		let minCount = 100000;
		for (let cache of caches) {
			minCount = Math.min(minCount, cache[i]);
		}
		if (minCount > 0 && minCount !== 100000) {
			while (minCount > 0) {
				res.push(alphabets[i]);
				minCount -= 1;
			}
		}
	}
	return res;
};
