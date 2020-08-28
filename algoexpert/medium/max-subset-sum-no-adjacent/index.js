function maxSubsetSumNoAdjacent(array) {
	if (array.length == 0) {
		return 0;
	}
	// Write your code here.
	const n = array.length;
	let choose = array[0];
	let notChoose = 0;
	for (let i = 1; i < n; i++) {
		const temp = choose;
		choose = Math.max(choose, notChoose + array[i]);
		notChoose = temp;
	}
	return Math.max(choose, notChoose);
}

// Do not edit the line below.
exports.maxSubsetSumNoAdjacent = maxSubsetSumNoAdjacent;
