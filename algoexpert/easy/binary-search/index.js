function binarySearch(array, target) {
	// Write your code here.
	let left = 0;
	let right = array.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target === array[mid]) {
			return mid;
		} else if (target < array[mid]) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	return -1;
}

// Do not edit the line below.
exports.binarySearch = binarySearch;
