/*
    1st approach: num sum
    - count the number of characters of each string and put it to the front of each string
        e.g. ['Hello', 'World'] -> 5>Hello5>World
    - when we see a [x], we regard the coming x characters as a string 

    Time    O(mn)
    Space   O(mn)
    104 ms, faster than 63.89%
*/
var encode = function (strs) {
	let res = "";
	for (let s of strs) {
		const count = s.length;
		res += count.toString() + ">" + s;
	}
	return res;
};
var decode = function (s) {
	const res = [];
	let i = 0;
	while (i < s.length) {
		let num = 0;
		while (s[i] != ">") {
			num = num * 10 + parseInt(s[i]);
			i += 1;
		}
		i += 1;
		let cur = "";
		for (let j = 0; j < num; j++) {
			cur += s[i];
			i += 1;
		}
		res.push(cur);
	}
	return res;
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */
