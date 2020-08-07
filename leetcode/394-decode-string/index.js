/*
    2nd approach: recursion

    Time    O(2n)
    Space   O(n)
    108 ms, faster than 6.34%
*/
var decodeString = function (s) {
	const q = [];
	for (let x of s) {
		q.push(x);
	}
	return recur(q);
};

const recur = (q) => {
	if (q.length === 0) {
		return "";
	}
	let s = "";
	let num = 0;
	while (q.length > 0) {
		const x = q.shift();
		if (parseInt(x) >= 0 && parseInt(x) < 10) {
			num = num * 10 + parseInt(x);
		} else if (x === "[") {
			const single = recur(q);
			for (let j = 0; j < num; j++) {
				s += single;
			}
			num = 0;
		} else if (x === "]") {
			return s;
		} else {
			s += x;
		}
	}
	return s;
};
