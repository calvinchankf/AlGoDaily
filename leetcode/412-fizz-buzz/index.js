/*
    1st approach: math

    Time    O(n)
    Space   O(n)
    84 ms, faster than 61.57%
*/
var fizzBuzz = function (n) {
	const res = [];
	for (let i = 1; i <= n; i++) {
		let s = "";
		if (i % 3 == 0) {
			s += "Fizz";
		}
		if (i % 5 == 0) {
			s += "Buzz";
		}
		if (s.length == 0) {
			res.push(i.toString());
		} else {
			res.push(s);
		}
	}
	return res;
};
