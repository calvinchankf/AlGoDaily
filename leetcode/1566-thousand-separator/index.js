/*
    1st: array
    - keep dividing the number by 10
    - maintain an index to see if we should add ,

    Time    O(N)
    Space   O(N)
    96 ms, faster than 100.00%
*/
var thousandSeparator = function (n) {
	if (n == 0) {
		return "0";
	}
	let j = 0;
	let res = "";
	while (n > 0) {
		const d = n % 10;
		if (j % 3 == 0 && res != "") {
			res = d + "." + res;
		} else {
			res = d + res;
		}
		j += 1;
		n = Math.floor(n / 10);
	}
	return res;
};
