/*
    1st: hashtable + sort

    Time    O(N + NlogN)
    Space   O(N)
*/
function largestRange(array) {
	const ht = new Set();
	for (let x of array) {
		ht.add(x);
	}
	let arr = [];
	for (let key of ht) {
		arr.push(key);
	}
	arr.sort((a, b) => a - b);
	let start = arr[0];
	let end = arr[0];
	let curStart = arr[0];
	let len = 1;
	for (let i = 1; i < arr.length; i++) {
		if (arr[i] == arr[i - 1] + 1) {
			len += 1;
		} else {
			curStart = arr[i];
			len = 1;
		}
		if (len > end - start + 1) {
			start = curStart;
			end = arr[i];
		}
	}
	return [start, end];
}

// Do not edit the line below.
// exports.largestRange = largestRange;

let a = [
	-7,
	-7,
	-7,
	-7,
	8,
	-8,
	0,
	9,
	19,
	-1,
	-3,
	18,
	17,
	2,
	10,
	3,
	12,
	5,
	16,
	4,
	11,
	-6,
	8,
	7,
	6,
	15,
	12,
	12,
	-5,
	2,
	1,
	6,
	13,
	14,
	-4,
	-2,
];
console.log(largestRange(a));

console.log("-----");

/*
    2nd: hashtable + expand left and right 
    - similar to lc5

    Time    O(N + N) liner time because every number could only be explored once in the course of expansion
    Space   O(N)
*/
function largestRange(array) {
	const used = {};
	for (let x of array) {
		used[x] = false;
	}
	let res = [array[0], array[0]];
	for (let x of array) {
		if (used[x] === true) {
			continue;
		}
		let left = x;
		let right = x;
		while (left - 1 in used) {
			left -= 1;
			used[left] = true;
		}
		while (right + 1 in used) {
			right += 1;
			used[right] = true;
		}
		const range = [left, right];
		if (right - left + 1 > res[1] - res[0] + 1) {
			res = range;
		}
	}
	return res;
}

console.log(largestRange(a));
