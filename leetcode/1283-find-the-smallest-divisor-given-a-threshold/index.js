/*
    1st: lower bound binary search
    - similar to lc778, 875, 1011, 1283, 1482, 1617
    - we have to find a point that the sum is <= threshold
    - look at the examples

    e.g.1 nums = [1,2,5,9], threshold = 6
    1 17
    2 10
    3 7
    4 7
    5 5 <- ans
    6 5

    e.g.2 nums = [2,3,5,7,11], threshold = 11
    1 28
    2 16
    3 11 <- ans
    4 9
    5 8
    6 7
    7 6
    8 6
    9 6
    10 6
    11 5

    e.g.3 nums = [19], threshold = 5
    1 19
    2 10
    3 7
    4 5 <- 5
    5 4


    Time    O(MlogN)
    Space   O(1)
    72 ms, faster than 98.96%
*/
var smallestDivisor = function (nums, threshold) {
	let left = 1;
	let right = 10 ** 6;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);

		let temp = 0;
		for (let i = 0; i < nums.length; i++) {
			temp += Math.ceil(nums[i] / mid);
		}

		if (temp <= threshold) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};
