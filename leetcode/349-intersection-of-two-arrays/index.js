/*
    1st: hashtable

    Time    O(M+N)
    Space   O(N)
    80 ms, faster than 60.20%
*/
var intersection = function (nums1, nums2) {
	const ht = {};
	for (let x of nums1) {
		ht[x] = true;
	}
	const res = new Set();
	for (let x of nums2) {
		if (x in ht) {
			res.add(x);
		}
	}
	return Array.from(res);
};
