function moveElementToEnd(array, toMove) {
	// Write your code here.
	const n = array.length;
	let j = n - 1;
	for (let i = n - 1; i >= 0; i--) {
		if (array[i] == toMove) {
			[array[i], array[j]] = [array[j], array[i]];
			j -= 1;
		}
	}
}

// Do not edit the line below.
// exports.moveElementToEnd = moveElementToEnd;

let a = [2, 1, 2, 2, 2, 3, 4, 2];
let b = 2;
moveElementToEnd(a, b);
console.log(a);
