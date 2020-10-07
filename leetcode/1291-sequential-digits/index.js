/*
    2nd: recursion

    Time    O(N)
    Space   O(N)
    72 ms, faster than 79.66%
*/
var sequentialDigits = function (low, high) {
	const candidates = [];

	const dfs = (n, k) => {
		if (k == 0) {
			return candidates.push(n);
		}
		const lastDigit = n % 10;
		if (lastDigit + 1 < 10) {
			dfs(n * 10 + lastDigit + 1, k - 1);
		}
	};

	for (let i = 1; i < 10; i++) {
		for (let j = 1; j < 10; j++) {
			dfs(j, i);
		}
	}

	const res = [];
	for (let i = 0; i < candidates.length; i++) {
		if (candidates[i] >= low && candidates[i] <= high) {
			res.push(candidates[i]);
		}
	}

	return res;
};
