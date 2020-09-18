/*
    1st approach: hashtable

    Time    O(M+N)
    Space   O(M)
    36 ms, faster than 52.13%
*/
var intersect = function (nums1, nums2) {
	const ht = {};
	for (let x of nums1) {
		if (x in ht) {
			ht[x] += 1;
		} else {
			ht[x] = 1;
		}
	}
	const res = [];
	for (let x of nums2) {
		if (x in ht) {
			const count = ht[x];
			if (count > 0) {
				res.push(x);
				ht[x] -= 1;
			}
		}
	}
	return res;
};
