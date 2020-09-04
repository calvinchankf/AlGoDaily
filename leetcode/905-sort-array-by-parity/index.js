/*
    1st: 2 pointers
    - similar to lc283
*/
var sortArrayByParity = function (A) {
	let j = 0;
	for (let i = 0; i < A.length; i++) {
		if (A[i] % 2 == 0) {
			[A[i], A[j]] = [A[j], A[i]];
			j += 1;
		}
	}
	return A;
};
