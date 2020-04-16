/**
 *  3rd attempt: shorten the 2nd approach by just using tuples as keys

    Time O(nk) n:number of words, k:length of charactors
    Space O(nk)
    136ms beats 70.28%

 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
	const ht = {};
	for (let s of strs) {
		const alphabetsCount = Array(26).fill(0);
		for (c of s) {
			const idx = c.charCodeAt(0) - 97;
			alphabetsCount[idx] += 1;
		}
		const key = alphabetsCount.join(",");
		if (ht[key] === undefined) {
			ht[key] = [s];
		} else {
			ht[key].push(s);
		}
	}
	const res = [];
	for (let key in ht) {
		res.push(ht[key]);
	}
	return res;
};
