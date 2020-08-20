/*
    3rd approach:
    - optimize the 2nd
    - use builtin sort

    Time    O(nlogn)
    Space   O(n)
    392 ms, faster than 72.84%
    10mar2019
*/
var kClosest = function (points, K) {
	const arr = [];
	for (let [x, y] of points) {
		const d = x ** 2 + y ** 2;
		arr.push([d, x, y]);
	}
	arr.sort((a, b) => a[0] - b[0]);
	const res = [];
	for (let i = 0; i < Math.min(K, arr.length); i++) {
		const coord = arr[i];
		res.push([coord[1], coord[2]]);
	}
	return res;
};
