/*
    2nd: 2 pointers
    - avoid using arrays
    - just iterate the strings from the back

    Time    O(M+N)
    Space   O(M+N) <- result
    92 ms, faster than 56.07% 
*/
var addStrings = function (num1, num2) {
	let carry = 0;
	let res = "";
	let i = num1.length - 1;
	let j = num2.length - 1;
	while (i >= 0 || j >= 0) {
		let a = 0;
		if (i >= 0) {
			a = parseInt(num1[i]);
			i -= 1;
		}
		let b = 0;
		if (j >= 0) {
			b = parseInt(num2[j]);
			j -= 1;
		}
		const c = a + b + carry;
		carry = Math.floor(c / 10);
		const d = c % 10;
		res = d + res;
	}
	if (carry > 0) {
		res = carry + res;
	}
	return res;
};
