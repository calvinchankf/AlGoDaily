/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 * 
 * 1st approach: zero sum subarray
    - this question is fucking similar to leetcode 325, 525, 523, 930
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: number of occurence of a previous sum
    - if currentSum - target in the hastable, the result += occurence

    e.g. [1, -1, 5, -2, 1, 2], 3
    when it comes to 2, remain = 6 - 3 = 3 and 3 is in the hashtable what does it mean?

    consider that a = [1,-1,5,-2] = 3,  b = [1, -1, 5, -2, 1, 2] = 6, 
    6-3 means the remain from a - b, which is [1,2], is = target k
    
    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time	O(n)
    Space   O(n)
    96 ms, faster than 51.22%
 */
var subarraySum = function (nums, k) {
	const m = {};
	let pfs = 0;
	let res = 0;
	for (let i = 0; i < nums.length; i++) {
		pfs += nums[i];
		if (pfs == k) {
			res += 1;
		}
		const remain = pfs - k;
		if (remain in m) {
			res += m[remain];
		}
		if (pfs in m) {
			m[pfs] += 1;
		} else {
			m[pfs] = 1;
		}
	}
	return res;
};
