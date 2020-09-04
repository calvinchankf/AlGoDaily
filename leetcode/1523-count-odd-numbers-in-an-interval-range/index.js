/*
    1st: math
    - update the boundaries to odd numbers
    - include negative

    Time    O(1)
    Space   O(1)
    68 ms, faster than 100.00%
*/
var countOdds = function (low, high) {
	if (low == high) {
		return low % 2;
	}
	const start = low % 2 == 0 ? low + 1 : low;
	const end = high % 2 == 0 ? high - 1 : high;
	if (start == end) {
		return start % 2;
	}
	return (end - start) / 2 + 1;
};

let a = -3;
let b = 3;
console.log(countOdds(a, b));

a = -4;
b = 3;
console.log(countOdds(a, b));

a = -4;
b = 4;
console.log(countOdds(a, b));
