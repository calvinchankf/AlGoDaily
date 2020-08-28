function selectionSort(array) {
	const n = array.length;
	// Write your code here.
	for (let i = 0; i < n; i++) {
		let minIdx = i;
		for (let j = i + 1; j < n; j++) {
			if (array[j] < array[minIdx]) {
				minIdx = j;
			}
		}
		[array[i], array[minIdx]] = [array[minIdx], array[i]];
	}
	return array;
}

// Do not edit the line below.
exports.selectionSort = selectionSort;
