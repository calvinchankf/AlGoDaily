/**
 * @param {number[]} digits
 * @return {number[]}
 * 
 *  1st approach: carry
    - like adding 2 big numbers
    
    Time    O(n)
    Space   O(1)
    52 ms, faster than 82.83%
 */
var plusOne = function (digits) {
	let carry = 1;
	const n = digits.length;
	for (let i = n - 1; i >= 0; i--) {
		const temp = digits[i] + carry;
		digits[i] = temp % 10;
		carry = Math.floor(temp / 10);
	}
	if (carry > 0) {
		digits = [carry, ...digits];
	}
	return digits;
};
