function bubbleSort(array) {
	// Write your code here.
	const n = array.length;
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n - 1; j++) {
			if (array[j] > array[j + 1]) {
				[array[j], array[j + 1]] = [array[j + 1], array[j]];
			}
		}
	}
	return array;
}

// Do not edit the line below.
exports.bubbleSort = bubbleSort;
