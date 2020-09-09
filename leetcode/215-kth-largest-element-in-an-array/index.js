/*
    1st approach: upper bound binary search

    Time    O(n * (logk + k)) since insert takes O(k)
    Space   O(k)
    88 ms, faster than 62.47% 
*/
var findKthLargest = function (nums, k) {
	const window = [];
	for (let x of nums) {
		const i = bsearch(window, x);
		window.splice(i, 0, x);
		if (window.length > k) {
			window.shift();
		}
	}
	return window[0];
};

const bsearch = function (nums, target) {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target >= nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};
