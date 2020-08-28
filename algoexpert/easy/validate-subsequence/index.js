/*
    2 pointers
*/
function isValidSubsequence(array, sequence) {
	// Write your code here.
	let j = 0;
	for (var i = 0; i < array.length; i++) {
		if (array[i] === sequence[j]) {
			j += 1;
		}
	}
	return i === array.length && j === sequence.length;
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;
