/*
    classic approach: Next lexicographical permutation algorithm(use a stack)

    similar to lc556

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
	80 ms, faster than 92.96%
*/
var nextPermutation = function (nums) {
    // Find non-increasing suffix
    const n = nums.length
	let i = n - 1;
	while (i > 0 && nums[i - 1] >= nums[i]) i--;

	if (i <= 0) {
		return reverse(nums, 0, n - 1);
	}

	// pivot
	const pivot = i - 1;

	// Find successor to pivot
	let j = n - 1;
	while (nums[j] <= nums[pivot]) j--;

	// swap the pivot and succesor
	[nums[pivot], nums[j]] = [nums[j], nums[pivot]];

	// Reverse suffix
	reverse(nums, i, n - 1);
};

const reverse = (nums, i, j) => {
	while (i < j) {
		[nums[j], nums[i]] = [nums[i], nums[j]];
		i += 1;
		j -= 1;
	}
};
