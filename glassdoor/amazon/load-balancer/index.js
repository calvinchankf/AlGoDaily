const f = (nums) => {
	const n = nums.length;
	const prefix_sums = Array(n).fill(0);
	const suffix_sums = Array(n).fill(0);

	let prefix_sum = 0;
	for (let i = 0; i < n; i++) {
		prefix_sum += nums[i];
		prefix_sums[i] = prefix_sum;
	}

	let suffix_sum = 0;
	for (let i = n - 1; i >= 0; i--) {
		suffix_sum += nums[i];
		suffix_sums[i] = suffix_sum;
	}

	let i = 0;
	let j = n - 1;
	while (i < j - 2) {
		const sum_from_left = prefix_sums[i];
		const sum_from_right = suffix_sums[j];
		const sum_in_middle = prefix_sums[j - 2] - prefix_sums[i + 1];
		if (sum_from_left == sum_from_right && sum_in_middle == sum_from_left) {
			return true;
		}
		if (sum_from_left < sum_from_right) {
			i += 1;
		} else if (sum_from_left > sum_from_right) {
			j -= 1;
		} else {
			i += 1;
			j -= 1;
		}
	}
	return false;
};

let a = [1, 3, 4, 2, 2, 2, 1, 1, 2];
console.log(f(a));

a = [1, 1, 1, 1, 1, 1];
console.log(f(a));

a = [];
for (let i = 0; i < 10000; i++) {
	a.push(1, 2);
}
console.log(f(a));

a = [1, 2, 3, 4, 4, 10, 2, 4, 1, 4, 1];
console.log(f(a));

a = [10, 4, 1, 2, 3, 4, 2, 4, 1, 4, 1];
console.log(f(a));
