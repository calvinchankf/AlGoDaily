/*
    1st: dp
    - similar to lc518 but diff loop arrangement

    Time    O(NA)
    Space   O(N)
    92 ms, faster than 35.05%
*/
var combinationSum4 = function (nums, target) {
	if (target == 0) {
		return 1;
	}
	const ways = Array(target + 1).fill(0);
	ways[0] = 1;
	for (let j = 1; j <= target; j++) {
		for (let c of nums) {
			const remain = j - c;
			if (remain >= 0) {
				ways[j] += ways[remain];
			}
		}
	}
	return ways[target];
};

/*
    2nd: recursion + hashtable
    - similar to lc1155
    - unlike coin change 1 & 2, here we need to find out all the combinations, 
    so it is eaiser to use the roll dice approach

    Time    O(NA)
    Space   O(N)
    420 ms, faster than 5.67%
*/
var combinationSum4 = function (nums, target) {
	const ht = {};
	const dfs = (path, remain) => {
		if (remain == 0) {
			return 1;
		}
		if (remain < 0) {
			return 0;
		}
		if (remain in ht) {
			return ht[remain];
		}
		let total = 0;
		for (let c of nums) {
			total += dfs([...path, c], remain - c);
		}
		ht[remain] = total;
		return total;
	};
	return dfs([], target);
};
