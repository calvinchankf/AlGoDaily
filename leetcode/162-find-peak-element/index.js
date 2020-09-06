/*
    2nd: upper bound binary search
    - compare with the previous item, if prev < cur, then search on the right handside

    e.g.1 [1,2,1,3,5,6,4]
                 ^          mid
                     ^      mid
                        ^   mid
    
    e.g.2 [1,6,5,4,3,2,1]
                 ^          mid
             ^              mid
               ^            mid

    Time    O(logN)
    Space   O(1)
    96 ms, faster than 15.38%
*/
var findPeakElement = function (nums) {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (nums[mid - 1] < nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	if (left <= 0) {
		return 0;
	}
	return left - 1;
};
