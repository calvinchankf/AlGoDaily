/*
    2nd: brute force recursion
    - there are duplicate results, so use a hashtable

    Time    O(2^N) every number has 2 options
    Space   O(2^N)
    96 ms, faster than 26.04%
*/
var readBinaryWatch = function (num) {
	const res = new Set();
	// const res = []

	const dfs = (n, hour, hi, minute, mi) => {
		if (n == 0) {
			if (minute < 10) {
				return res.add(`${hour}:0${minute}`);
				// return res.push(`${hour}:0${minute}`)
			}
			return res.add(`${hour}:${minute}`);
			// return res.push(`${hour}:${minute}`)
		}
		for (let i = hi; i < 4; i++) {
			if (hour + 2 ** i < 12) {
				dfs(n - 1, hour + 2 ** i, i + 1, minute, mi);
			}
		}
		for (let i = mi; i < 6; i++) {
			if (minute + 2 ** i < 60) {
				dfs(n - 1, hour, hi, minute + 2 ** i, i + 1);
			}
		}
	};
	dfs(num, 0, 0, 0, 0);

	return Array.from(res);
};

/*
    3rd: better brute force recursion
    - no duplicate value here because we use one fromIdx from the bottom

    Time    O(2^N) every number has 2 options
    Space   O(2^N)
    96 ms, faster than 26.04%
*/
var readBinaryWatch = function (num) {
	const res = [];

	const dfs = (n, hour, minute, fromIdx) => {
		if (n == 0) {
			if (minute < 10) {
				return res.push(`${hour}:0${minute}`);
			}
			return res.push(`${hour}:${minute}`);
		}
		for (let i = fromIdx; i < 10; i++) {
			if (i < 4) {
				if (hour + 2 ** i < 12) {
					dfs(n - 1, hour + 2 ** i, minute, i + 1);
				}
			} else {
				const j = i - 4;
				if (minute + 2 ** j < 60) {
					dfs(n - 1, hour, minute + 2 ** j, i + 1);
				}
			}
		}
	};
	dfs(num, 0, 0, 0);

	return res;
};
