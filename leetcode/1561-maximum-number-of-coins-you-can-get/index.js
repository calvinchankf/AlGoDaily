/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function (piles) {
	piles.sort((a, b) => b - a);
	let res = 0;
	let i = 1;
	while (i < Math.floor((piles.length * 2) / 3)) {
		res += piles[i];
		i += 2;
	}
	return res;
};
