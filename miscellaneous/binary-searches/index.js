const bsearch = (nums, target) => {
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
	// to find number that <= target
	// return right

	// to find number that >= target
	// return left
	return -1;
};

console.log("--bsearch--");
console.log(bsearch([1, 3, 5, 7, 9], 4)); // -1
console.log(bsearch([1, 3, 5, 7, 9], 5)); // 2

const recursiveBsearch = (nums, target) => {
	const f = (left, right) => {
		const mid = Math.floor((left + right) / 2);
		if (target == nums[mid]) {
			return mid;
		} else if (target < nums[mid]) {
			return f(left, mid - 1);
		} else {
			return f(left + 1, mid);
		}
	};
	return f(0, nums.length - 1);
};

console.log("--recursiveBsearch--");
console.log(bsearch([1, 3, 5, 7, 9], 4)); // -1
console.log(bsearch([1, 3, 5, 7, 9], 5)); // 2

const bSearchNearest = (nums, target) => {
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
};

console.log("--bSearchNearest--");
console.log(bSearchNearest([1, 3, 7, 13, 20], 4)); // 1
console.log(bSearchNearest([1, 3, 7, 13, 20], 5)); // 2

const lowerBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target <= nums[mid]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};

console.log("--lowerBsearch--");
console.log(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 0)); // 0
console.log(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 1)); // 0
console.log(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 4)); // 2 <-
console.log(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 5)); // 2 <-
console.log(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 10)); // 7
// 1. the first num at index that >= target
// 2. how many numbers < k

const upperBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target >= nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};

console.log("--upperBsearch--");
console.log(upperBsearch([1, 3, 5, 5, 5, 7, 9], 0)); // 0
console.log(upperBsearch([1, 3, 5, 5, 5, 7, 9], 5)); // 5 <-
console.log(upperBsearch([1, 3, 5, 5, 5, 7, 9], 6)); // 5 <-
console.log(upperBsearch([1, 3, 5, 5, 5, 7, 9], 10)); // 7
// e.g. how many numbers <= k
