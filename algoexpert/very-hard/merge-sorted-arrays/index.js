function mergeSortedArrays(arrays) {
	// Write your code here.
	let final = [...arrays[0]];

	const merge2Arrays = (nums1, nums2) => {
		let res = [];
		let i = 0;
		let j = 0;
		while (i < nums1.length && j < nums2.length) {
			if (nums1[i] < nums2[j]) {
				res.push(nums1[i]);
				i += 1;
			} else {
				res.push(nums2[j]);
				j += 1;
			}
		}
		if (i < nums1.length) {
			res = res.concat(nums1.slice(i));
		}
		if (j < nums2.length) {
			res = res.concat(nums2.slice(j));
		}
		return res;
	};

	for (let i = 1; i < arrays.length; i++) {
		final = merge2Arrays(final, arrays[i]);
	}

	return final;
}

// Do not edit the line below.
exports.mergeSortedArrays = mergeSortedArrays;
