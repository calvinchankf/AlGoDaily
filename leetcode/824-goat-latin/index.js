/*
    1st approach: hashset + string manipulation

    Time    O(n) n: number of words in sentence
    Space   O(S) the result
    100 ms, faster than 16.11%
*/
var toGoatLatin = function (S) {
	const vowels = new Set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]);
	let res = "";
	const words = S.split(" ");
	for (let i = 0; i < words.length; i++) {
		let w = words[i];
		if (!vowels.has(w[0])) {
			w = w.slice(1) + w[0];
		}
		res += w + "ma" + "a".repeat(i + 1) + " ";
	}
	return res.slice(0, res.length - 1);
};
