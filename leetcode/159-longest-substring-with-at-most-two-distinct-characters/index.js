/*
    1st: 2pointers + hashtable
    - similar to lc3, 340, 904
    - maintain the sliding window to have 2 unique keys

    Time    O(N)
    Space   O(N)
    148 ms, faster than 15.16%
*/
var lengthOfLongestSubstringTwoDistinct = function (s) {
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

		while (Object.keys(ht).length > 2) {
			const last = s[slow];
			ht[last] -= 1;
			slow += 1;
			if (ht[last] == 0) {
				delete ht[last];
			}
		}
		res = Math.max(res, i - slow + 1);
	}
	return res;
};
