/*
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    320 ms, faster than 83.63%
*/
var findDisappearedNumbers = function (nums) {
	const hs = new Set(nums);
	const res = [];
	for (let i = 1; i <= nums.length; i++) {
		if (!hs.has(i)) {
			res.push(i);
		}
	}
	return res;
};

/*
    2nd: mutate the array
    - since it is from 1 to N, all positive
    - for every number, we can change the nums[i] to a negative number
    - then for each of the possitive number at an arbitary index, it is not being mutated by some other numbers. It means this index is disappeared

    Time    O(n)
    Space   O(1)
    112 ms, faster than 86.74%
*/
var findDisappearedNumbers = function (nums) {
	for (let i = 0; i < nums.length; i++) {
		const x = Math.abs(nums[i]);
		const target = x - 1;
		if (nums[target] > 0) {
			nums[target] *= -1;
		}
	}
	const res = [];
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] > 0) {
			res.push(i + 1);
		}
	}
	return res;
};
