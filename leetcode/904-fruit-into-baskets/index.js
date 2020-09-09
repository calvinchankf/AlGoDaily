/*
    1st approach: sliding window
    - exactly the same question lc159

    The question is so confusing, lets rephrase the quesion:
    Given a string, find the max length of a substring which has only 2 distinct characters
	e.g. "ababacddc", return 5
	becos length of "ababa" = 5, where all other substrings are < 5
	e.g.
	length of "abab" = 4
	length of "cddc" = 4
	.
    .
    .

	To solve this,
	1. we can use 2 pointers to indicate the left and right
	2. if the substring btw left and right has more than 2 keys, move the left forwad until the substring has 2 keys

	Time	O(2n)
	Space	O(m) m: number of the distinct characters
	472 ms, faster than 22.03%
*/
var totalFruit = function (tree) {
	let ht = {};
	let slow = 0;
	let res = 0;
	for (let i = 0; i < tree.length; i++) {
		const x = tree[i];

		if (x in ht) {
			ht[x] += 1;
		} else {
			ht[x] = 1;
		}

		while (Object.keys(ht).length > 2) {
			const last = tree[slow];
			ht[last] -= 1;
			slow += 1;
			if (ht[last] == 0) {
				delete ht[last];
			}
		}
		res = Math.max(res, i - slow + 1);
	}
	return res;
};
