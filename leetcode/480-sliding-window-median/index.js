/*
    1st approach
    - binary search to 
        - pop the left most item
        - push the right most item to the window
    - therefore to optimize the window sliding

    Time    O(n*2k)
    Space   O(k)
    108 ms, faster than 88.31%
*/
var medianSlidingWindow = function (nums, k) {
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
			const median = calMedian(sortedWindow);
			res.push(median);
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

const calMedian = (nums) => {
	const half = Math.floor((nums.length - 1) / 2);
	if (nums.length % 2 == 0) {
		return (nums[half] + nums[half + 1]) / 2.0;
	} else {
		return nums[half] * 1.0;
	}
};
