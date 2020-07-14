/*
    2nd approach: math % and /

    Time  O(3logN) log base are 2, 3, 5
    Space O(1)
    76 ms, faster than 81.07%
*/

var isUgly = function (num) {
	if (num < 1) {
		return false;
	}
	while (num % 2 == 0) {
		num /= 2;
	}
	while (num % 3 == 0) {
		num /= 3;
	}
	while (num % 5 == 0) {
		num /= 5;
	}
	return num === 1;
};
