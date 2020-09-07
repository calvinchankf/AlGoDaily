/*
    1st: array + hashtable
    - assume the input is legit all the time, then we dont need to care about e.g. MID

    Time    O(N)
    Space   O(1)
    152 ms, faster than 87.83% 
*/
var romanToInt = function (s) {
	const ht = {
		I: 1,
		V: 5,
		X: 10,
		L: 50,
		C: 100,
		D: 500,
		M: 1000,
	};
	let res = 0;
	const n = s.length;
	for (let i = 0; i < n; i++) {
		res += ht[s[i]];
		if (i > 0 && ht[s[i - 1]] < ht[s[i]]) {
			res -= ht[s[i - 1]] * 2;
		}
	}
	return res;
};
