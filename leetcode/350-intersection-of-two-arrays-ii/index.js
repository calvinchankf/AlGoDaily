/*
    1st approach: hashtable

    Time    O(A+B)
    Space   O(A+B)
    88 ms, faster than 38.10% 
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
