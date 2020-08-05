/*
    1st: binary search
    
    Time    O(logN)
    Space   O(1)
    116 ms, faster than 22.03%
*/
var arrangeCoins = function (n) {
	let left = 1;
	let right = n + 1;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (n >= f(mid)) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left - 1;
};

var f = function (x) {
	return ((x + 1) * x) / 2;
};
