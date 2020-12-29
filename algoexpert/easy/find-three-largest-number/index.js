function findThreeLargestNumbers(array) {
	// Write your code here.
	let largest = Number.MIN_SAFE_INTEGER;
	let largest2 = Number.MIN_SAFE_INTEGER;
	let largest3 = Number.MIN_SAFE_INTEGER;
	for (let x of array) {
		if (x > largest) {
			largest3 = largest2;
			largest2 = largest;
			largest = x;
		} else if (x > largest2) {
			largest3 = largest2;
			largest2 = x;
		} else if (x > largest3) {
			largest3 = x;
		}
	}
	return [largest3, largest2, largest];
}

// Do not edit the line below.
exports.findThreeLargestNumbers = findThreeLargestNumbers;
