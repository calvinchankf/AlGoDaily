/*
    in-place version
    - similar to lc283, 75

    ref:
    - https://gist.github.com/imwally/58d6bb9bf9da098064054f73a19cdca1
    - https://www.youtube.com/watch?v=COk73cpQbFQ

    Worst Time		O(n^2): findHalf might need to iterate the rest of the array for each item
    Average	Time	O(nlogn)
    Space 				O(h)
*/
function quickSort(array) {
	// Write your code here.
	quicksort(array, 0, array.length - 1);
	return array;
}

const quicksort = (nums, start, end) => {
	if (start < end) {
		const partitionIdx = partition(nums, start, end);
		quicksort(nums, start, partitionIdx - 1);
		quicksort(nums, partitionIdx + 1, end);
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
exports.quickSort = quickSort;
