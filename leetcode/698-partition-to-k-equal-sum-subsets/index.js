/*
    1st approach: backtracking
    - the naive approach is to explore all the subsets, O(2^n), but for each item we can use once only
    , so we need to cache the used item(by store the indices)
    - so we need to do backtracking(similar to lc51, 52)
        - try to include the next number
        - and 'backtrack' the next number if it fails
    - if we reach to the point where our curSum == target, we set k=k-1 and explore again from the begining of the input array 

    ref:
    - https://www.youtube.com/watch?v=qpgqhp_9d1s
    - https://segmentfault.com/a/1190000017013991
    - https://github.com/cherryljr/LeetCode/blob/master/Partition%20to%20K%20Equal%20Sum%20Subsets.java

    Time    from O(2^n) to O(n!) i actually dont know to determind
    Space   O(n) depth of recursion tree
    432ms beats 34%
*/
var canPartitionKSubsets = function (nums, k) {
	let total = 0;
	for (let x of nums) {
		total += x;
	}
	if (total % k != 0) {
		return false;
	}
	const target = Math.floor(total / k);
	const used = Array(nums.length).fill(false);

	const dfs = (fromIdx, _k, remain) => {
		if (_k == 1) {
			return true;
		}
		if (remain == 0) {
			return dfs(0, _k - 1, target);
		}
		for (let i = fromIdx; i < nums.length; i++) {
			if (used[i] == false) {
				used[i] = true;
				if (dfs(i + 1, _k, remain - nums[i])) {
					return true;
				}
				used[i] = false;
			}
		}
		return false;
	};

	return dfs(0, k, target);
};
