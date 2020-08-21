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

    concern: will A[mid-1] be out of bound?

    - in short, no!
    - in detail, because the question guarantees that the array has at least 3 items. 
    
    Lets look at the example: [0,10,2]
    
    left = 0, right = 3, then mid = 1 -----> since A[0] = 0 and A[1] = 10, left = left + 1 = 1 + 1 = 2
    left = 2, right = 3, then mid = 2 -----> since A[1] = 10 and A[2] = 2, right = mid = 2
    left = 2, right = 2, then exit while loop

    Both left&right point to 2, which is the number that next to the peak(similar to upper bound binary search)

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
