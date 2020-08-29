/*
    binary search
*/
function smallestDifference(arrayOne, arrayTwo) {
	// Write your code here.
	arrayTwo.sort((a, b) => a - b);

	let one = -1;
	let two = -1;
	for (let i = 0; i < arrayOne.length; i++) {
		let x = arrayOne[i];
		let j = bsearch(arrayTwo, x);
		let y = arrayTwo[j];
		let diff = Math.abs(x - y);
		if (
			(one === -1 && two === -1) ||
			diff < Math.abs(arrayOne[one] - arrayTwo[two])
		) {
			one = i;
			two = j;
		}
	}
	return [arrayOne[one], arrayTwo[two]];
}

function bsearch(nums, target) {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target == nums[mid]) {
			return mid;
		} else if (target < nums[mid]) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	// bounds checking
	if (right < 0) {
		return 0;
	}
	if (left > nums.length - 1) {
		return nums.length - 1;
	}
	if (Math.abs(target - nums[right]) < Math.abs(target - nums[left])) {
		return right;
	}
	return left;
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;
