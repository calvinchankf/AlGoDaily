/*
    1st: array
    - basically, we can just observe the number of bit changes along the way we iterrate the string
    - thats it

    Time    O(N)
    Space   O(N)
    84 ms, faster than 93.97%
*/
var minFlips = function (target) {
	let s = "0" + target;
	let res = 0;
	for (let i = 1; i < s.length; i++) {
		if (s[i - 1] !== s[i]) {
			res += 1;
		}
	}
	return res;
};
