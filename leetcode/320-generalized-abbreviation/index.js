/*
    2nd approach: recursion similar to 1st
    - BUT here we used # represent the count so that we dont have to deal with the corner cases like b13 -> 14

    Time    O(n2^n) <= O(2^n) each character has 2 options(number OR to stay). O(n) transform a###b##c# to a3b2c1
    Space   O(2^n)
    316 ms, faster than 9.09%
*/
var generateAbbreviations = function (word) {
	const seen = new Set();
	const res = [];

	const transform = (s) => {
		let res = "";
		let count = 0;
		for (let i = 0; i < s.length; i++) {
			if (s[i] === "#") {
				count += 1;
			} else {
				if (count > 0) {
					res += count.toString();
					count = 0;
				}
				res += s[i];
			}
		}
		if (count > 0) {
			res += count.toString();
			count = 0;
		}
		return res;
	};

	const dfs = (s) => {
		if (seen.has(s)) {
			return;
		}
		seen.add(s);

		res.push(transform(s));

		for (let i = 0; i < s.length; i++) {
			const x = s[i].toLowerCase();
			const idx = x.charCodeAt(0) - "a".charCodeAt(0);
			if (idx < 0 || idx > 25) {
				continue;
			}
			dfs(s.slice(0, i) + "#" + s.slice(i + 1));
		}
	};
	dfs(word);

	return res;
};

console.log(generateAbbreviations("word"));

console.log(generateAbbreviations("prescribed"));
