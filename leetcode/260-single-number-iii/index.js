/*
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    88 ms, faster than 35.87%
*/
var singleNumber = function (nums) {
	const ht = {};
	for (let x of nums) {
		if (ht[x] === undefined) {
			ht[x] = 1;
		} else {
			delete ht[x];
		}
	}
	const res = [];
	for (let key in ht) {
		res.push(key);
	}
	return res;
};
