/*
    1st approach: min and max 2 arrays
    - similar to lc42, 135, 487, 1493
    - from the front to the end, store the max at each index
    - from the end to the front, store the min at each index
    - when max[i-1] <= max[i] <= min[i+1], it is the target index of the last item in the winter period

    e.g. 1
            5, 0, 3, 8, 6
    max ->  5, 5, 5, 8, 8
    min <-  3, 3, 3, 6, 6
                    ^
                    this is the partition point

    e.g. 2
            1, 1, 1, 0, 6, 12
    max ->  1, 1, 1, 1, 6, 12
    min <-  0, 0, 0, 0, 6, 12
                       ^
                       this is the partition point

    Time    O(3n)
    Space   O(2n)
    96 ms, faster than 45.71% 
*/
var partitionDisjoint = function (A) {
	const n = A.length;
	const forwards = Array(n).fill(0);
	const backwards = Array(n).fill(0);

	let runningMax = 0;
	for (let i = 0; i < n; i++) {
		runningMax = Math.max(runningMax, A[i]);
		forwards[i] = runningMax;
	}

	let runningMin = 10 ** 6;
	for (let i = n - 1; i >= 0; i--) {
		runningMin = Math.min(runningMin, A[i]);
		backwards[i] = runningMin;
	}

	for (let i = 0; i < n - 1; i++) {
		if (forwards[i] <= backwards[i + 1]) {
			return i + 1;
		}
	}
};
