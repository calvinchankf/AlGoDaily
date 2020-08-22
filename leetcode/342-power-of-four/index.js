/*
    1st approach: log

    64 = 4^3
    3 = log(64)/log(4)

    Time    O(1)
    Space   O(1)
    72 ms, faster than 96.24%
*/
var isPowerOfFour = function (num) {
	if (num < 1) {
		return false;
	}
	const temp = Math.floor(Math.log(num) / Math.log(4));
	return num == 4 ** temp;
};

/*
    2nd: math
    Time    O(logN)
    Space   O(1)
    92 ms, faster than 58.82%
*/
var isPowerOfFour = function (num) {
	while (num > 1) {
		if (num % 4 !== 0) {
			return false;
		}
		num /= 4;
	}
	return num === 1;
};
