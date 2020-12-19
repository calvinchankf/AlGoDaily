const abs = Math.abs;
const floor = Math.floor;

/*
    1st approach: binary search
	- for each pair, we look for the remain
	e.g. [1,2,3,4,5] 10
	for pair 1,2, search 7 within [3,4,5]
	for pair 1,3, search 6 within [4,5]

	Time		O(n^2logn)
	Space		O(1)
	148 ms, faster than 15.98%
*/
var threeSumClosest = function (nums, target) {
	const n = nums.length;
	nums.sort((a, b) => a - b);

	let res = Number.MAX_SAFE_INTEGER;

	for (let i = 0; i < n; i++) {
		for (let j = i + 1; j < n; j++) {
			const remain = target - (nums[i] + nums[j]);
			const idx = bsearch(nums, remain);
			if (idx != i && idx != j) {
				const cur = nums[i] + nums[j] + nums[idx];
				if (abs(cur - target) < abs(res - target)) {
					res = cur;
				}
			}
		}
	}
	return res;
};

const bsearch = (nums, target) => {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = floor((left + right) / 2);
		if (target < nums[mid]) {
			right = mid - 1;
		} else if (target > nums[mid]) {
			left = mid + 1;
		} else {
			return mid;
		}
	}
	if (right < 0) {
		return 0;
	}
	if (left > nums.length - 1) {
		return nums.length - 1;
	}
	if (abs(nums[left] - target) < abs(nums[right] - target)) {
		return left;
	}
	return right;
};

const abs = Math.abs;
const floor = Math.floor;

/*
    2nd approach: 2 pointers
	- e.g. [2,3,6,10], 10
	pair=0,3, sum = 12, diff=+2, right--
	pair=0,2, sum = 8, diff=-2, left++
	pair=1,2, sum = 9, diff=-1, cannot move any pointers
    ...
    
    reminder:
    - since closest means the result can be either smaller or bigger than the target,
        the 2 pointers loop ends only either: 
        - left == right
        - OR total == target

	Time		O(n^2)
	Space		O(1)
	72 ms, faster than 96.85%
*/
var threeSumClosest = function (nums, target) {
	const n = nums.length
    nums.sort((a, b) => a - b)
    
    let res = Number.MAX_SAFE_INTEGER
    
    for (let i = 0; i < n; i++) {
        let left = i + 1
        let right = n - 1
        while (left < right) {
            const total = nums[i] + nums[left] + nums[right]
            if (abs(total - target) < abs(res - target)) {
                res = total
            }
            if (total < target) {
                left += 1
            } else if (total > target) {
                right -= 1
            } else {
                return total
            }
        }
    }
    return res
};
