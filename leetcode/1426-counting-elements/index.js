/**
 * @param {number[]} arr
 * @return {number}
 */
var countElements = function (arr) {
	const hs = {};
	arr.forEach((x) => {
		hs[x] = true;
	});
	let res = 0;
	arr.forEach((x) => {
		if (hs[x + 1] == true) {
			res += 1;
		}
	});
	return res;
};
