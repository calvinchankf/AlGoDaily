/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
	if (nums1.length == m) {
		return nums1;
	}

	let x = nums1.length - 1;
	for (let i = m - 1; i >= 0; i--) {
		nums1[x] = nums1[i];
		nums1[i] = 0;
		x -= 1;
	}

	let i = nums1.length - m;
	let j = 0;
	let k = 0;
	while (i < nums1.length && j < n) {
		if (nums1[i] <= nums2[j]) {
			nums1[k] = nums1[i];
			i += 1;
			k += 1;
		} else {
			nums1[k] = nums2[j];
			j += 1;
			k += 1;
		}
	}
	while (i < nums1.length) {
		nums1[k] = nums1[i];
		i += 1;
		k += 1;
	}
	while (j < n) {
		nums1[k] = nums2[j];
		j += 1;
		k += 1;
	}
};
