/*
    2nd approach: binary search
    - use binary search to maintain a sorted list(window) all the array to the end
    - each window maximum is the last item in each window 

    Time  O(nlogk) -> O(nk)
    Space O(k)
    2520 ms, faster than 15.90%
*/
var maxSlidingWindow = function (nums, k) {
	const window = [];
	const sortedWindow = [];
	const res = [];
	for (let i = 0; i < nums.length; i++) {
		window.push(nums[i]);
		const idx = upperBsearch(sortedWindow, nums[i]);
		sortedWindow.splice(idx, 0, nums[i]);

		if (window.length > k) {
			const last = window.shift();
			const idx = lowerBsearch(sortedWindow, last);
			sortedWindow.splice(idx, 1);
		}

		if (sortedWindow.length == k) {
			res.push(sortedWindow[sortedWindow.length - 1]);
		}
	}
	return res;
};

const lowerBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target <= nums[mid]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};

const upperBsearch = (nums, target) => {
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
