/*
    1st: hashtable
    
    Time    O(N)
    Space   O(N)
    144 ms, faster than 45.54%
*/
var findDuplicates = function (nums) {
	const res = [];
	const hs = new Set();
	for (let x of nums) {
		if (hs.has(x)) {
			res.push(x);
		} else {
			hs.add(x);
		}
	}
	return res;
};
