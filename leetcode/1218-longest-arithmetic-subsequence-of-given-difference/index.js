/*
    1st: dyanamic programming with hashtable
    - similar to lc560 but witout prefix sum
    - related to lc1027
    - use a hashtable to store the { distinct number : max length of a sequence }

    e.g.
    [1, 5, 7, 8, 5, 3, 4, 2, 1], -2
     1  1  1  1  2  3  1  2  4       <- for each number, find if ht[x-dff] exists and update ht[x] with the max length of a sequence
    
    Time    O(N)
    Space   O(N)
    212 ms, faster than 30.77%
*/
var longestSubsequence = function (arr, difference) {
	const ht = {};
	let res = 0;
	for (let x of arr) {
		const prev = x - difference;
		if (prev in ht) {
			ht[x] = Math.max(isNaN(ht[x]) ? 0 : ht[x], ht[prev] + 1);
		} else {
			ht[x] = 1;
		}
		res = Math.max(res, ht[x]);
	}
	return res;
};
