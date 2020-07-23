/*
    2nd: sort

    Time    O(NlogN)
    Space   O(1)
    88 ms, faster than 100.00%
*/
var average = function (salary) {
	salary.sort((a, b) => a - b);
	salary = salary.slice(1, salary.length - 1);
	let total = 0;
	for (let x of salary) {
		total += x;
	}
	return total / salary.length;
};
