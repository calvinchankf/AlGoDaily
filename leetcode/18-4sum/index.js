/*
    2nd approach: 2 pointers
	1. sort the numbers to make sure that the key will be unique
	2. for each num[i] + num[j], use 2 pointers, from the front and from the end, to find the pairs which nums[i]+nums[j]+nums[start]+nums[end] sum up to target
	3. use a set to deduplicate

	Time	O(n^3)
	Space	O(n)
	176 ms, faster than 26.33%
*/
var fourSum = function (nums, target) {
	nums.sort((a, b) => a - b);
	const res = new Map();
	for (let h = 0; h < nums.length; h++) {
		for (let i = h + 1; i < nums.length; i++) {
			let left = i + 1;
			let right = nums.length - 1;
			while (left < right) {
				const sum = nums[h] + nums[i] + nums[left] + nums[right];
				if (sum === target) {
					const k = `${nums[h]}, ${nums[i]}, ${nums[left]}, ${nums[right]}`;
					const v = [nums[h], nums[i], nums[left], nums[right]];
					res.set(k, v);
					left += 1;
					right -= 1;
				} else if (sum < target) {
					left += 1;
				} else {
					right -= 1;
				}
			}
		}
	}
	const yo = [];
	for (let [k, v] of res) {
		yo.push(v);
	}
	return yo;
};
