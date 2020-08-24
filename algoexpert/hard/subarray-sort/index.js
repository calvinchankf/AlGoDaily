/*
    sort
*/
function subarraySort(array) {
	// Write your code here.
	sorted = [...array];
	sorted.sort((a, b) => a - b);

	console.log(array);
	console.log(sorted);

	let left = -1;
	for (let i = 0; i < array.length; i++) {
		if (array[i] !== sorted[i]) {
			left = i;
			break;
		}
	}

	let right = -1;
	for (let i = array.length - 1; i >= 0; i--) {
		if (array[i] !== sorted[i]) {
			right = i;
			break;
		}
	}

	if (left >= right) {
		return [-1, -1];
	}
	return [left, right];
}

// Do not edit the line below.
exports.subarraySort = subarraySort;
