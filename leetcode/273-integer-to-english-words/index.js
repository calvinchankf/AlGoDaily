/*
    1st approach:
	1. separate the number portion by portion with 3 digits, 123456789 -> 123, 456, 789
	2. for each 3 digits, translate to english
	3. append Thousand, Million and Billion in between the portions

	Time		O(n)
	Space		O(n)
	0 ms, faster than 100.00%
	26feb2019
*/
var numberToWords = function (num) {
	if (num == 0) {
		return "Zero";
	}
	const scales = ["", "Thousand", "Million", "Billion"];
	let res = "";
	let i = 0;
	while (num > 0) {
		const mod = num % 1000;
		num = Math.floor(num / 1000);
		const threeDigitWords = getThreeDigitWords(mod);
		if (threeDigitWords.length > 0) {
			res = threeDigitWords + " " + scales[i] + " " + res;
		}
		i += 1;
	}
	return res.trim();
};

var getThreeDigitWords = function (num) {
	const digits = [
		"",
		"One",
		"Two",
		"Three",
		"Four",
		"Five",
		"Six",
		"Seven",
		"Eight",
		"Nine",
		"Ten",
		"Eleven",
		"Twelve",
		"Thirteen",
		"Fourteen",
		"Fifteen",
		"Sixteen",
		"Seventeen",
		"Eighteen",
		"Nineteen",
	];
	const tens = [
		"",
		"",
		"Twenty",
		"Thirty",
		"Forty",
		"Fifty",
		"Sixty",
		"Seventy",
		"Eighty",
		"Ninety",
	];
	const a = Math.floor(num / 100);
	const bc = num % 100;
	let res = "";
	if (a > 0) {
		res = digits[a] + " Hundred";
	}
	if (bc < 20) {
		res += " " + digits[bc];
	} else {
		const b = Math.floor(bc / 10);
		const c = bc % 10;
		res += " " + tens[b];
		res += " " + digits[c];
	}
	return res.trim();
};
