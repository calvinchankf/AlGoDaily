/*
    1st approach: min and max 2 arrays
    - similar to lc42, 135, 487, 1493
    - from the front to the end, store the max at each index
    - from the end to the front, store the min at each index
    - when max[i-1] <= max[i] <= min[i+1], it is the target index of the last item in the winter period

    Time    O(3n)
    Space   O(2n)
    96 ms, faster than 45.71% 
*/
var partitionDisjoint = function (A) {
	const n = A.length;
	const forwards = Array(n).fill(0);
	let fmax = 0;
	for (let i = 0; i < n; i++) {
		fmax = Math.max(fmax, A[i]);
		forwards[i] = fmax;
	}

	const backwards = Array(n).fill(10 ** 6);
	let bmin = 10 ** 6;
	for (let i = n - 1; i >= 0; i--) {
		bmin = Math.min(bmin, A[i]);
		backwards[i] = bmin;
	}
	for (let i = 0; i < n - 1; i++) {
		if (forwards[i] <= backwards[i + 1]) {
			return i + 1;
		}
	}
};
