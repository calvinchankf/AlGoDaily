/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function (arr) {
	const seen = {};
	for (let i = 0; i < arr.length; i++) {
		seen[arr[i]] = i;
	}
	for (let i = 0; i < arr.length; i++) {
		const target = arr[i] * 2;
		if (target in seen && seen[target] != i) {
			return true;
		}
	}
	return false;
};
