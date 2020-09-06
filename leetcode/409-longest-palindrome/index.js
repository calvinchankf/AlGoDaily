/*
    1st approach: hashtable
    1. count the occurence of each character
    2. make sure the all characters occurr "evenly" by declementing the odd ocurrence characters
    3. if no of odd ocurrence characters > 0, 
        wit means that we have to place any one of them in the center to form the biggest palindrome

    Time    O(n)
    Space   O(n)
    84 ms, faster than 51.69%
*/
var longestPalindrome = function (s) {
	const ht = {};
	for (let c of s) {
		if (c in ht) {
			ht[c] += 1;
		} else {
			ht[c] = 1;
		}
	}

	let biggestOddCount = 0;
	let biggestOddKey = "";
	for (let key in ht) {
		if (ht[key] % 2 == 1 && ht[key] > biggestOddCount) {
			biggestOddCount = ht[key];
			biggestOddKey = key;
		}
	}

	let res = 0;
	for (let key in ht) {
		if (ht[key] % 2 == 0) {
			res += ht[key];
		} else if (key == biggestOddKey) {
			res += ht[key];
		} else {
			res += ht[key] - 1;
		}
	}

	return res;
};
