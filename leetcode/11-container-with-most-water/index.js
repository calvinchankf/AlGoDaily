/*
    2nd approach
	- 2 pointers: one from the front, one from the end
	- move inward by retaining the heightest amongst the arr[i] and arr[j]
	- https://leetcode.com/articles/container-with-most-water/
    
	Time		O(n)
	Space		O(1)
    92 ms, faster than 50.53%
*/
var maxArea = function (heights) {
	let res = 0;
	let left = 0;
	let right = heights.length - 1;
	while (left < right) {
		const h = Math.min(heights[left], heights[right]);
		const w = right - left;
		res = Math.max(res, h * w);
		if (heights[left] < heights[right]) {
			left += 1;
		} else {
			right -= 1;
		}
	}
	return res;
};
