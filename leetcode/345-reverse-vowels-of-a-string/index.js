/*
    1st approach: 2 pointers

    Time  O(n)
    Space O(n)
    176 ms, faster than 17.26%
*/
var reverseVowels = function (s) {
	const n = s.length;
	let i = 0;
	let j = n - 1;
	const chars = s.split("");
	while (i < j) {
		const a = isVowel(chars[i]);
		const b = isVowel(chars[j]);
		if (a && b) {
			[chars[i], chars[j]] = [chars[j], chars[i]];
			i += 1;
			j -= 1;
		} else if (a) {
			j -= 1;
		} else if (b) {
			i += 1;
		} else {
			i += 1;
			j -= 1;
		}
	}
	return chars.join("");
};

const isVowel = (c) => {
	const hs = new Set(["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]);
	return hs.has(c);
};
