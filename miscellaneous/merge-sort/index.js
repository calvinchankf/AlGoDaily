/*
    merge sort: https://www.geeksforgeeks.org/merge-sort/
    - divides input array into two halves recursively
    - merge two sorted halves and then return
    - this version occupies space(not in-place)
    - first divide, second process; the procedure is similar to post order traversal
    
    Time	O(nlogn)
    Space   O(n)
*/
function mergeSort(array) {
	return divide(array);
}

const divide = (nums) => {
	if (nums.length == 1) {
		return nums;
	}
	const mid = Math.floor(nums.length / 2);
	const leftArr = divide(nums.slice(0, mid));
	const rightArr = divide(nums.slice(mid));
	return conquer(leftArr, rightArr);
};

const conquer = (leftArr, rightArr) => {
	const res = [];
	let i = 0;
	let j = 0;
	while (i < leftArr.length && j < rightArr.length) {
		if (leftArr[i] < rightArr[j]) {
			res.push(leftArr[i]);
			i += 1;
		} else {
			res.push(rightArr[j]);
			j += 1;
		}
	}
	while (i < leftArr.length) {
		res.push(leftArr[i]);
		i += 1;
	}
	while (j < rightArr.length) {
		res.push(rightArr[j]);
		j += 1;
	}
	return res;
};

// Do not edit the line below.
exports.mergeSort = mergeSort;
