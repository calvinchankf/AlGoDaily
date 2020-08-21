/*
    Approach 1b: hashtable, wrap 2sum with one more loop
	1. sort the numbers to make sure that the key will be unique
	2. put the numbers in a hashtable, num:index as key:value
	3. for each nums[i] + nums[j], find out the num from the hashtable that they sum up to zero
	4. use a set to deduplicate

    Time    O(NlogN + N^2 + N)
    Space   O(N)

    311 / 313 test cases passed.
    TLE...wtf?
*/
var threeSum = function (nums) {
	nums.sort((a, b) => a - b);
	// console.log(nums)
	const resultHt = {};
	const n = nums.length;
	// console.log(n)
	for (let i = 0; i < n; i++) {
		if (i > 0 && nums[i] == nums[i - 1]) {
			continue;
		}
		// console.log(i)
		const ht = {};
		for (let j = i + 1; j < n; j++) {
			const remain = -nums[i] - nums[j];

			if (remain in ht) {
				const k = ht[remain];
				const key = `${nums[i]},${nums[k]},${nums[j]}`;
				resultHt[key] = [nums[i], nums[k], nums[j]];
			}
			ht[nums[j]] = j;
		}
	}
	// console.log(resultHt)
	const res = [];
	for (let k in resultHt) {
		res.push(resultHt[k]);
	}
  return res
};


/*
  2nd: 2 pointers
  Time    O(NlogN + N^2 + N)
  Space   O(N)
  148 ms, faster than 71.53%
*/
var threeSum = function (nums) {
	nums.sort((a, b) => a - b);
	const res = [];
	for (let i = 0; i < nums.length - 2; i++) {
		if (i > 0 && nums[i] == nums[i - 1]) {
			continue;
		}
		let left = i + 1;
		let right = nums.length - 1;
		while (left < right) {
			const sum = nums[i] + nums[left] + nums[right];
			if (sum === 0) {
				res.push([nums[i], nums[left], nums[right]]);
				while (left < right && nums[left] == nums[left + 1]) {
					left += 1;
				}
				left += 1;
				while (left < right && nums[right - 1] == nums[right]) {
					right -= 1;
				}
				right -= 1;
			} else if (sum < 0) {
				left += 1;
			} else {
				right -= 1;
			}
		}
	}
	return res;
};
