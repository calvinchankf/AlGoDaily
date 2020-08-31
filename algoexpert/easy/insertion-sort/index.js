function insertionSort(array) {
	// Write your code here.
	for (let i = 1; i < array.length; i++) {
		const cur = array[i];
		for (let j = i - 1; j >= 0; j--) {
			if (cur < array[j]) {
				array[j + 1] = array[j];
				array[j] = cur;
			}
		}
	}
	return array;
}

// Do not edit the line below.
exports.insertionSort = insertionSort;
