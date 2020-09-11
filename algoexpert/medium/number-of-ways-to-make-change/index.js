function numberOfWaysToMakeChange(amount, coins) {
	// Write your code here.
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
}

// Do not edit the line below.
exports.numberOfWaysToMakeChange = numberOfWaysToMakeChange;
