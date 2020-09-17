function quickselect(array, k) {
	// Write your code here.
	if (k <= 0 || k > array.length) {
		return null;
	}
	const idx = quicksort(array, 0, array.length - 1, k);
	return array[idx];
}

const quicksort = (nums, start, end, k) => {
	const partitionIdx = partition(nums, start, end);
	if (k - 1 == partitionIdx) {
		return partitionIdx;
	} else if (k - 1 < partitionIdx) {
		return quicksort(nums, start, partitionIdx - 1, k);
	} else {
		return quicksort(nums, partitionIdx + 1, end, k);
	}
};

const partition = (nums, start, end) => {
	const pivot = nums[end];
	let partitionIdx = start;
	for (let i = start; i < end; i++) {
		if (nums[i] <= pivot) {
			[nums[i], nums[partitionIdx]] = [nums[partitionIdx], nums[i]];
			partitionIdx += 1;
		}
	}
	// after the for loop, all numbers on the left-hand side of pIdx <= pivot
	// so now we can put the pivit at pIdx
	[nums[end], nums[partitionIdx]] = [nums[partitionIdx], nums[end]];
	return partitionIdx;
};

// Do not edit the line below.
exports.quickselect = quickselect;
