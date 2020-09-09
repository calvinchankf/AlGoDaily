/*
    2nd approach: check substrings
	- when we encounter different characters at the same index, compare the remaining substrings

	There're 3 possibilities to satisfy the question:
	1) Replace 1 char:
 	  s: a X b c
 	  t: a Y b c
    2) Delete 1 char from s:
        s: a X  b c
        t: a    b c
    3) Delete 1 char from t
        s: a   b c
        t: a X b c

	Time		O(min(S,T))
	Space		O(1)
    76 ms, faster than 83.33%
*/
var isOneEditDistance = function (s, t) {
	const minL = Math.min(s.length, t.length);
	for (let i = 0; i < minL; i++) {
		if (s[i] != t[i]) {
			if (s.length == t.length) {
				return s.slice(i + 1) == t.slice(i + 1);
			} else if (s.length < t.length) {
				return s.slice(i) == t.slice(i + 1);
			} else if (s.length > t.length) {
				return s.slice(i + 1) == t.slice(i);
			}
		}
	}
	if (Math.abs(s.length - t.length) == 1) {
		return true;
	}
	return false;
};
