/*
    1st: recursive dfs

    e.g. [1,2,3]
    1          2         3
    2,3 3,2   1,3  3,1    1,2 2,1

    - select k from n number, it is a permutation problem therefore, 
        the time complexity is nPk = n!/(n-k)!

    - the crux is dfs(nums[:i]+arr[i+1:], prefix+[nums[i]])
    
    84 ms, faster than 85.31%
*/
var permute = function (nums) {
	var res = [];
	const f = (cands, chosen) => {
		if (cands.length === 0) {
			res.push(chosen);
		}
		for (let i = 0; i < cands.length; i++) {
			let left = cands.slice(0, i);
			let right = cands.slice(i + 1);
			f([...left, ...right], [...chosen, cands[i]]);
		}
	};
	f(nums, []);

	return res;
};
