/*
    1st approach: array

    Time    O(n) number of nums
    Space   O(1)
    80 ms, faster than 39.43%
*/
var findMissingRanges = function (nums, lower, upper) {
	if (lower > upper) {
		return [];
	}
	const clone = [lower - 1, ...nums, upper + 1];
	const res = [];
	for (let i = 1; i < clone.length; i++) {
		if (clone[i] > clone[i - 1] + 1) {
			if (clone[i - 1] + 1 == clone[i] - 1) {
				res.push(`${clone[i - 1] + 1}`);
			} else {
				res.push(`${clone[i - 1] + 1}->${clone[i] - 1}`);
			}
		}
	}
	return res;
};

/*  
    2nd: 2 pass
    
    Time    O(2N)
    Space   O(N)
    80ms beats 38.04%
*/
var findMissingRanges = function(nums, lower, upper) {
    const intvs = []
    nums = [lower-1, ...nums, upper+1]
    for (let i = 1; i < nums.length; i++) {
        const left = nums[i-1] + 1
        const right = nums[i] - 1
        if (left <= right) {
            intvs.push([left, right])
        }
    }
    const res = []
    for (let [s, e] of intvs) {
        if (s == e) {
            res.push(`${s}`)
        } else {
            res.push(`${s}->${e}`)
        }
    }
    return res
};