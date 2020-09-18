/*
    2nd approach: reduce B to a single word
    - reduce B to a single word
    - see if a contains that single word

    Time    O(A+B)
    Space   O(A+B)
    1180 ms, faster than 64.90%
*/
var wordSubsets = function (A, B) {
	const ht = Array(26).fill(0);
	for (let b of B) {
		const temp = Array(26).fill(0);
		for (let c of b) {
			const idx = c.charCodeAt(0) - "a".charCodeAt(0);
			temp[idx] += 1;
		}
		for (let i = 0; i < ht.length; i++) {
			ht[i] = Math.max(ht[i], temp[i]);
		}
	}

	const res = [];
	for (let a of A) {
		const cur = Array(26).fill(0);
		for (let c of a) {
			const idx = c.charCodeAt(0) - "a".charCodeAt(0);
			cur[idx] += 1;
		}
		let shouldAdd = true;
		for (let i = 0; i < ht.length; i++) {
			if (cur[i] < ht[i]) {
				shouldAdd = false;
				break;
			}
		}
		if (shouldAdd) {
			res.push(a);
		}
	}
	return res;
};
