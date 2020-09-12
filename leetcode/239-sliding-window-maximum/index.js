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

/*
    3rd: deque(double-ended queue) <- suggested approach

    - the idea is monotonic queue: when you push an element, a monotonic queue pop all the items smaller than that 
    e.g. [1,3,-1,-3,5,3,6,7]

                                window          max
    [1] 3 -1 -3 5 3 6 7         [1]             n/a
    [1 3] -1 -3 5 3 6 7         [3]             n/a
    [1 3 -1] -3 5 3 6 7         [3, -1]         3
    1 [3 -1 -3] 5 3 6 7         [3,-1,-3]       3
    1 3 [-1 -3 5] 3 6 7         [5]             5
    1 3 -1 [-3 5 3] 6 7         [5,3]           5
    1 3 -1 -3 [5 3 6] 7         [6]             6
    1 3 -1 -3 5 [3 6 7]         [7]             7


    Time    O(2N)
    Space   O(N)
    372 ms, faster than 51.72%
*/
var maxSlidingWindow = function (nums, k) {
	const n = nums.length;
	if (n * k == 0) {
		return [];
	} else if (k == 1) {
		return nums;
	}

	const window = [];
	const res = [];
	for (let i = 0; i < n; i++) {
		// clean window
		if (window.length > 0 && window[0] == i - k) {
			window.shift();
		}

		while (window.length > 0 && nums[window[window.length - 1]] < nums[i]) {
			window.pop();
		}

		// add current indx
		window.push(i);

		if (i + 1 >= k) {
			const first = window[0];
			res.push(nums[first]);
		}
	}
	return res;
};
