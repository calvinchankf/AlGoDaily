/*
    1st approach: classic bit op
    - for any number which is 2^k, there is only one one
    e.g.
    8  = 1000
    32 = 10000

    Time    O(32)
    Space   O(1)
    92 ms, faster than 56.19%
*/
var isPowerOfTwo = function (n) {
	if (n <= 0) {
		return false;
	}
	isOneExisted = false;
	while (n > 0) {
		if (n & (1 == 1)) {
			if (isOneExisted) {
				return false;
			}
			isOneExisted = true;
		}
		n >>= 1;
	}
	return true;
};

/*
    2nd approach: math
    - divide by 2 until mod != 0

    Time    O(logn)
    Space   O(1) 
    80 ms, faster than 85.90% 
*/
var isPowerOfTwo = function (n) {
	if (n <= 0) {
		return false;
	}
	while (n > 1) {
		const m = n % 2;
		if (m !== 0) {
			return false;
		}
		n /= 2;
	}
	return true;
};
