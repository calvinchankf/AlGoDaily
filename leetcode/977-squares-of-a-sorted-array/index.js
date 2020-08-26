/*
    1st:
    - to avoid using sort, merge 2 arrays by putting the smaller item in iteratively

    Time    O(N)
    Space   O(N)
    120 ms, faster than 73.42%
*/
var sortedSquares = function (A) {
	const negs = [];
	const poss = [];
	for (let i = 0; i < A.length; i++) {
		if (A[i] < 0) {
			negs.push(A[i] ** 2);
		} else {
			poss.push(A[i] ** 2);
		}
	}
	negs.reverse();
	const res = [];
	let i = 0;
	let j = 0;
	while (i < negs.length && j < poss.length) {
		if (negs[i] < poss[j]) {
			res.push(negs[i]);
			i += 1;
		} else {
			res.push(poss[j]);
			j += 1;
		}
	}
	while (i < negs.length) {
		res.push(negs[i]);
		i += 1;
	}
	while (j < poss.length) {
		res.push(poss[j]);
		j += 1;
	}
	return res;
};
