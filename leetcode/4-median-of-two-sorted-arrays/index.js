/*
    2nd approach: 2 pointers to merge the arrays like merge arrays
	- use 2 pointers to merge the arrays and return merged[half] or (merged[half-1]+merged[half])/2

	Time		O(m+n)
	Space 	    O(m+n)
	136 ms, faster than 63.17%
*/
var findMedianSortedArrays = function (nums1, nums2) {
	let arr = [];
	let p1 = 0;
	let p2 = 0;
	let n1 = nums1.length;
	let n2 = nums2.length;
	while (p1 < n1 && p2 < n2) {
		if (nums1[p1] < nums2[p2]) {
			arr.push(nums1[p1]);
			p1 += 1;
		} else {
			arr.push(nums2[p2]);
			p2 += 1;
		}
	}
	if (p1 < n1) {
		arr = [...arr, ...nums1.slice(p1)];
	} else if (p2 < n2) {
		arr = [...arr, ...nums2.slice(p2)];
	}
	if (arr.length % 2 === 0) {
		const mid = arr.length / 2;
		const left = arr[mid - 1];
		const right = arr[mid];
		return (left + right) / 2.0;
	}
	const mid = Math.floor(arr.length / 2);
	return arr[mid];
};
