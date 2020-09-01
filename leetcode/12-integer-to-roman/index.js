/*
    2nd approach:
    - split cases for 1-3,4,5,6-8,9

    Time    O(n)
    Space   O(n)
    152 ms, faster than 87.83%
*/
var intToRoman = function (num) {
	const ht = {
		1: "I",
		4: "IV",
		5: "V",
		9: "IX",
		10: "X",
		40: "XL",
		50: "L",
		90: "XC",
		100: "C",
		400: "CD",
		500: "D",
		900: "CM",
		1000: "M",
	};
	let res = "";
	let count = 0;
	while (num > 0) {
		const digit = num % 10;
		const x = digit * 10 ** count;
		num = Math.floor(num / 10);
		if (x in ht) {
			res = ht[x] + res;
		} else if (digit > 1 && digit < 4) {
			res = ht[10 ** count].repeat(digit) + res;
		} else if (digit > 5 && digit < 9) {
			res = ht[5 * 10 ** count] + ht[10 ** count].repeat(digit - 5) + res;
		}
		count += 1;
	}
	return res;
};
