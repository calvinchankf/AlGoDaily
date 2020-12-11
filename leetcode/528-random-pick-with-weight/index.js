/*
    1st: binary search
    e.g. [1,5,2]

    Prefix-sum array: [1,6,8]

    Consider any number from 1 to 8, we should get 
    [1,2,3,4,5,6,7,8]
    [0,1,1,1,1,1,1,2] <- we should always get 1 when we search from 2 to 7 inclusive

    Clearly, we can do it with a binary search to find number that >= target

    Time of init()          O()
    Time of pickIndex()     O(logN)
    Space                   O(N)
    200 ms, faster than 67.32% 
*/
var Solution = function (w) {
	this.nums = [];
	let pfs = 0;
	for (let x of w) {
		pfs += x;
		this.nums.push(pfs);
	}
};

Solution.prototype.pickIndex = function () {
	const r = Math.floor(Math.random() * this.nums[this.nums.length - 1]) + 1;
	return bsearch(this.nums, r);
};

const bsearch = (nums, target) => {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target == nums[mid]) {
			return mid;
		} else if (target < nums[mid]) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	// to find number that >= target
	return left;
};

/*
    ES6 version + lower bound binary search
*/
class Solution {
    constructor(w) {
        this.nums = []
        let pfs = 0
        for (let x of w) {
            pfs += x
            this.nums.push(pfs)
        }
    }
    pickIndex() {
        const last = this.nums[this.nums.length-1]
        const x = Math.floor(Math.random() * last) + 1 // from 1 to K instead of 0 to K-1
        const i = this._lowerBsearch(this.nums, x)
        return i
    }
    _lowerBsearch(nums, target) {
        let left = 0
        let right = nums.length
        while (left < right) {
            const mid = Math.floor((left + right) / 2)
            if (target <= nums[mid]) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}