/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {string}
 */
var longestDiverseString = function (a, b, c) {
	return dfs(a, b, c, "a", "b", "c");
};

function dfs(a, b, c, aa, bb, cc) {
	if (a < b) return dfs(b, a, c, bb, aa, cc);
	if (b < c) return dfs(a, c, b, aa, cc, bb);

	const an = Math.min(2, a);
	if (b === 0) {
		return aa.repeat(an);
	}

	let bn = Math.min(2, b);
	if (a - an > b) {
		bn = 1;
	}

	return aa.repeat(an) + bb.repeat(bn) + dfs(a - an, b - bn, c, aa, bb, cc);
}

console.log(longestDiverseString(1, 1, 7));

function dfs(
	largestRemain,
	largest2Remain,
	smallestRemain,
	largestChar,
	largest2Char,
	smallestChar
) {
	if (largestRemain < largest2Remain) {
		return dfs(
			largest2Remain,
			largestRemain,
			smallestRemain,
			largest2Char,
			largestChar,
			smallestChar
		);
	}
	if (largest2Remain < smallestRemain) {
		return dfs(
			largestRemain,
			smallestRemain,
			largest2Remain,
			largestChar,
			smallestChar,
			largest2Char
		);
	}

	const largestCount = Math.min(2, largestRemain);
	if (largest2Remain === 0) {
		return largestChar.repeat(largestCount);
	}

	let largest2Count = Math.min(2, largest2Remain);
	if (largestRemain - largestCount > largest2Remain) {
		largest2Count = 1;
	}

	return (
		largestChar.repeat(largestCount) +
		largest2Char.repeat(largest2Count) +
		dfs(
			largestRemain - largestCount,
			largest2Remain - largest2Count,
			smallestRemain,
			largestChar,
			largest2Char,
			smallestChar
		)
	);
}

console.log(longestDiverseString(1, 1, 7));
