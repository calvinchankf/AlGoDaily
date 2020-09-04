/*
    1st: brute force

    Time    O(KlogN) K depends on the number
    Space   O(1)
    96 ms, faster than 47.33%
*/
var addDigits = function (num) {
	let cur = num;
	while (cur > 9) {
		cur = f(cur);
	}
	return cur;
};

const f = (num) => {
	let res = 0;
	while (num > 0) {
		res += num % 10;
		num = Math.floor(num / 10);
	}
	return res;
};

/*
    2nd: math
    - this is unpragmatic, no one should ask this

    ref:
    - https://en.wikipedia.org/wiki/Digital_root#Congruence_formula

    Time    O(1)
    Space   O(1)
    88 ms, faster than 73.76%
*/
var addDigits = function (num) {
	return 1 + ((num - 1) % 9);
};
