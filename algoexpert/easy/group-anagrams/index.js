function groupAnagrams(words) {
	// Write your code here.
	const ht = {};
	for (let s of words) {
		const alphabetsCount = Array(26).fill(0);
		for (let c of s) {
			const idx = c.charCodeAt(0) - "a".charCodeAt(0);
			alphabetsCount[idx] += 1;
		}
		const key = alphabetsCount.join(",");
		if (key in ht) {
			ht[key].push(s);
		} else {
			ht[key] = [s];
		}
	}
	const res = [];
	for (let key in ht) {
		res.push(ht[key]);
	}
	return res;
}

// Do not edit the line below.
exports.groupAnagrams = groupAnagrams;
