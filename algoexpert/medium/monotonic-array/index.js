/*
    1st: iteration

    Time    O(N)
    Space   O(1)
*/
function isMonotonic(array) {
	// Write your code here.
	let gDir = null;
	for (let i = 1; i < array.length; i++) {
		const temp = array[i] - array[i - 1];
		let dir = 0;
		if (temp > 0) {
			dir = 1;
		} else if (temp < 0) {
			dir = -1;
		}
		if (dir === 0) {
			continue;
		}
		if (gDir === 0) {
			gDir = dir;
		} else if (gDir !== dir) {
			return false;
		}
	}
	return true;
}

// Do not edit the line below.
exports.isMonotonic = isMonotonic;
