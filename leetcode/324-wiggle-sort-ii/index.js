/*
    1st approach: sort similar to lc280
    - sort it, and then split them and put the numbers back to the array

    e.g. even
    [1,3,2,2] 
    
    1. sort
    => [1,2,2,3] < if we do it like lc280, we will have [1,2,2,3] as a result
    
    2. split 
    => [1,2], [2,3]
    
    3. reverse 2nd/stackpop
    => [2,1], [3,2]
    reason: we want to make sure that the end of the 1st half wont collide with the start of the 2nd half, in this case, the 2

    4. result
    [2,3,1,2]

    Time    O(nlogn)
    Space   O(n)
    120 ms, faster than 66.35%
*/
var wiggleSort = function (nums) {
	const n = nums.length;
	if (n == 0) {
		return [];
	}
	const arr = [...nums];
	arr.sort((a, b) => a - b);
	const half = Math.ceil(n / 2);
	const a = arr.slice(0, half); // a is longer in length
	const b = arr.slice(half);
	for (let i = 0; i < n; i++) {
		if (i % 2 == 0) {
			// if the length of an array is odd, the last index must be an even
			nums[i] = a.pop();
		} else {
			nums[i] = b.pop();
		}
	}
};
