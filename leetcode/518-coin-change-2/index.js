/*
    3rd: 2d array DP

    ref: 
    - https://www.youtube.com/watch?v=DJ4a7cmjZY0
    - https://www.youtube.com/watch?v=jaNZ83Q3QGc
    - https://leetcode.com/problems/coin-change-2/discuss/674977/100-Faster-or-Recursive-1-d-2-d-DP-or-Matrix-With-Example-or-Commented
*/
var change = function (amount, coins) {
	if (amount == 0) {
		return 1;
	}
	const ways = Array(amount + 1).fill(0);
	ways[0] = 1;
	for (let c of coins) {
		for (let j = 1; j <= amount; j++) {
			const remain = j - c;
			if (j - c >= 0) {
				ways[j] += ways[j - c];
			}
		}
	}
	return ways[amount];
};
