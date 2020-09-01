/*
    Time    O(N)
    Space   O(N)
    84 ms, faster than 30.13%
*/
var lengthOfLastWord = function (s) {
	if (s.length == 0) {
		return 0;
	}
	const words = s.trim().split(" ");
	return words[words.length - 1].length;
};
