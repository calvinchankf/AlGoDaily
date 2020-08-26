/*
    2nd approach: 2 pointers
	
    e.g.1 [2,3,6,10], 10
	pair=0,3, sum = 12, diff=+2, right--
	pair=0,2, sum = 8, diff=-2, left++ => count++
	pair=1,2, sum = 9, diff=-1, cannot move any pointers => count++
	...

    e.g.2 [1, 3, 4, 5, 7, 9, 10], 13

    at index 0, [1, 3, 4, 5, 7, 9, 10]
                 *  ^        ^          count += 3 becase (1,3,4), (1,3,5), (1,3,7) then left += 1
    
    at index 0, [1, 3, 4, 5, 7, 9, 10]
                 *     ^     ^          count += 2 because (1,4,5), (1,4,7) then left += 1

    at index 1, [1, 3, 4, 5, 7, 9, 10]
                    *  ^  ^             count += 1 becase (3,4,5)
    
    Staring from index 2, num[i] + nums[left] + nums[right] no more less than target
    , so the result = 6

	Time		O(n^2)
	Space		O(1)
    108 ms, faster than 34.44%
*/
var threeSumSmaller = function (nums, target) {
	const n = nums.length;
	nums.sort((a, b) => a - b);

	let res = 0;

	for (let i = 0; i < n; i++) {
		let left = i + 1;
		let right = n - 1;
		while (left < right) {
			const total = nums[i] + nums[left] + nums[right];
			if (total < target) {
				res += right - left;
				left += 1;
			} else {
				right -= 1;
			}
		}
	}
	return res;
};
