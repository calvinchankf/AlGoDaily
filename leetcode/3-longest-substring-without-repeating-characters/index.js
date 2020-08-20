/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
	let ht = {};
	let slow = 0;
	let res = 0;
	for (let i = 0; i < s.length; i++) {
		const x = s[i];
		if (x in ht) {
			ht[x] += 1;
		} else {
			ht[x] = 1;
		}
		while (ht[x] > 1) {
			const last = s[slow];
			ht[last] -= 1;
			if (ht[last] == 0) {
				delete ht[last];
			}
			slow += 1;
		}
		res = Math.max(res, i - slow + 1);
	}
	return res;
};
