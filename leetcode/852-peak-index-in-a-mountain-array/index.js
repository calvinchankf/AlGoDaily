/*
    1st: 2 arrays

    Time    O(3N)
    Space   O(2N)
    120 ms, faster than 6.26%
*/
var peakIndexInMountainArray = function (A) {
	const n = A.length;

	const forwards = Array(n).fill(false);
	forwards[0] = true;
	for (let i = 1; i < n - 1; i++) {
		forwards[i] = A[i - 1] < A[i] && forwards[i - 1] === true;
	}

	const backwards = Array(n).fill(false);
	backwards[n - 1] = true;
	for (let i = n - 2; i >= 0; i--) {
		backwards[i] = A[i + 1] < A[i] && backwards[i + 1] === true;
	}

	for (let i = 1; i < n - 1; i++) {
		if (forwards[i] && backwards[i]) {
			return i;
		}
	}
};

/*
    2nd: upper boundy binary search

    Time    O(logN)
    Space   O(1)
    88 ms, faster than 11.15%
*/
var peakIndexInMountainArray = function (A) {
	let left = 0;
	let right = A.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (A[mid - 1] < A[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left - 1;
};
