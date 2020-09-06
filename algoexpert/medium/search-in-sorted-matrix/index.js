function searchInSortedMatrix(matrix, target) {
	// Write your code here.
	const n = matrix.length;
	for (let i = 0; i < n; i++) {
		const j = bsearch(matrix[i], target);
		if (j > -1) {
			return [i, j];
		}
	}
	return [-1, -1];
}

const bsearch = (nums, target) => {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target < nums[mid]) {
			right = mid - 1;
		} else if (target > nums[mid]) {
			left = mid + 1;
		} else {
			return mid;
		}
	}
	return -1;
};

// Do not edit the line below.
exports.searchInSortedMatrix = searchInSortedMatrix;
