/*
    2nd approach: sliding window
    - check if each substring is an anagram but dont use slice in every iteration

    Time    O(n*m)
    Space   O(m)
    208 ms, faster than 37.02% 
*/
var findAnagrams = function (s, p) {
	const pMask = computeMask(p);
	const curMask = Array(26).fill(0);

	let res = [];
	let slow = 0;
	for (let i = 0; i < s.length; i++) {
		const c = s[i];
		const x = c.charCodeAt(0) - "a".charCodeAt(0);
		curMask[x] += 1;
		if (i - slow >= p.length) {
			const last = s[slow];
			const y = last.charCodeAt(0) - "a".charCodeAt(0);
			curMask[y] -= 1;
			slow += 1;
		}

		let found = true;
		for (let i = 0; i < 26; i++) {
			if (pMask[i] != curMask[i]) {
				found = false;
				break;
			}
		}
		if (found) {
			res.push(slow);
		}
	}
	return res;
};

const computeMask = (s) => {
	const mask = Array(26).fill(0);
	for (let c of s) {
		const x = c.charCodeAt(0) - "a".charCodeAt(0);
		mask[x] += 1;
	}
	return mask;
};
