/*
    1st: top-down recursion with memoization using hashtable
    - find the subset which has the sum of total//2
    - cache the result from the bottom, i.e. (currentIdx, remainTarget), to avoid redundant calculation

    Time    O(NS) N: number of nums, S: the total sum of all the numbers
    Space   O(h)
    112 ms, faster than 54.99%
*/
var canPartition = function (nums) {
	let total = 0;
	for (let x of nums) {
		total += x;
	}
	if (total % 2 == 1) {
		return false;
	}

	const target = Math.floor(total / 2);
	return dfs(nums, 0, target, {});
};

const dfs = (nums, fromIdx, remain, ht) => {
	if (remain === 0) {
		return true;
	}
	if (remain < 0) {
		return false;
	}
	const key = `${fromIdx},${remain}`;
	if (key in ht) {
		return ht[key];
	}
	for (let i = fromIdx; i < nums.length; i++) {
		if (dfs(nums, i + 1, remain - nums[i], ht)) {
			return true;
		}
	}
	ht[key] = false;
	return false;
};

/*
    2nd approach: top-down recursion with memoization using hashtable
    - every number has 2 options
    - but we can cache the result of the combinations of remainTarget and currentIdx to avoid redundant calculation

    ref:
    - https://en.wikipedia.org/wiki/Partition_problem
    - https://www.educative.io/collection/page/5668639101419520/5633779737559040/5752754626625536

    Time    O(NS) N: number of nums, S: the total sum of all the numbers
    Space   O(h)
    5696 ms, faster than 5.07% 
*/
var canPartition = function (nums) {
	let total = 0;
	for (let x of nums) {
		total += x;
	}
	if (total % 2 == 1) {
		return false;
	}

	const target = Math.floor(total / 2);
	return dfs(nums, 0, target, {});
};

const dfs = (nums, fromIdx, remain, ht) => {
	if (remain === 0) {
		return true;
	}
	if (fromIdx === nums.length || remain < 0) {
		return false;
	}
	const key = `${fromIdx},${remain}`;
	if (key in ht) {
		return ht[key];
	}
	const pick = dfs(nums, fromIdx + 1, remain - nums[fromIdx], ht);
	const notPick = dfs(nums, fromIdx + 1, remain, ht);
	const b = pick || notPick;
	ht[key] = b;
	return b;
};
