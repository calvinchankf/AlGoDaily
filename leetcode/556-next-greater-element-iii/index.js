/*
    classic approach: Next lexicographical permutation algorithm(use a stack)

    similar to lc31

	e.g. 43143221
	- find the non-increasing suffix, e.g. 431<43221>
	- once it encounters a smaller number from the end, this is the target we want
		e.g. 43 <1> 43221
	- i need to swap the target with the value in the stack which is just larger then it
		e.g. 43 <1> 43221
                       ^
         => 43 <2> 43211
                      ^
	- reverse the right half and put it back to the number
		e.g. 43 <2> 43211 => 43 <2> 11234
	- combine them together and form the result
		e.g. 43 <2> 11234 => 43211234

	ref:
	- https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

	Time	O(n)
	Space	O(n)
	8 ms, faster than 100.00%
*/
var nextGreaterElement = function (n) {
	const s = n.toString();
	const nums = s.split("");

	// find the monotonic increasing suffix
	let i = nums.length - 1;
	while (i - 1 >= 0 && nums[i - 1] >= nums[i]) i--;
	if (i == 0) {
		return -1;
	}

	// pivot is the num next to the suffix
	const pivot = i - 1;

	// find the successor
	let j = nums.length - 1;
	while (j >= i && nums[j] <= nums[pivot]) j--;

	// swap the numbers at pivot and the successor
	[nums[pivot], nums[j]] = [nums[j], nums[pivot]];

	// reverse the suffix
	reverse(nums, i, nums.length - 1);

	const res = nums.join("");
	if (res > 2 ** 31 - 1) {
		return -1;
	}
	return res;
};

const reverse = (nums, i, j) => {
	while (i < j) {
		[nums[j], nums[i]] = [nums[i], nums[j]];
		i += 1;
		j -= 1;
	}
};
