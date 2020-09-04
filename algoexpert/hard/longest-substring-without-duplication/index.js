/*
    - lc3
    - print the substring as well
*/
function longestSubstringWithoutDuplication(s) {
	// Write your code here.
	const ht = {};
	let j = 0;
	let gDiff = 0;
	let resI = 0;
	let resJ = 0;
	for (let i = 0; i < s.length; i++) {
		const c = s[i];

		if (c in ht) {
			ht[c] += 1;
		} else {
			ht[c] = 1;
		}

		while (ht[c] > 1) {
			const last = s[j];
			j += 1;
			ht[last] -= 1;
			if (ht[last] == 0) {
				delete ht[last];
			}
		}

		const diff = i - j + 1;
		if (diff > gDiff) {
			gDiff = diff;
			resI = i;
			resJ = j;
		}
	}
	return s.slice(resJ, resI + 1);
}

// Do not edit the line below.
exports.longestSubstringWithoutDuplication = longestSubstringWithoutDuplication;
