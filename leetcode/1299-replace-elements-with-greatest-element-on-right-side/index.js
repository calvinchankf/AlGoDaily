/*
    1st:
    1. iterate the array from the back
    2. put the running max value into the result array
    3. update the running max value if the current item is larger

    Time    O(N)
    Space   O(1)
    84 ms, faster than 55.42%
*/
var replaceElements = function (arr) {
	const n = arr.length;
	let curMax = -1;
	const res = Array(n).fill(-1);
	for (let i = n - 1; i >= 0; i--) {
		res[i] = curMax;
		curMax = Math.max(curMax, arr[i]);
	}
	return res;
};
