/*
    2nd approach:
    - there are total 2^2n permutation we when appedn ( and ) from top to down
    - however, some resulting parentheses strings are not balenced
    - to make it balence, we should set a constraint that no. of close <= no. of open

    Time    < O(2^2n) the total number of nodes in the recursion tree
    Space   < O(2^2n)
    64 ms, faster than 96.56%
*/
var generateParenthesis = function (n) {
	if (n <= 0) {
		return [];
	}

	const res = [];
	const f = (s, open, close) => {
		if (open == n && close == n) {
			res.push(s);
		}
		if (open + 1 <= n) {
			f(s + "(", open + 1, close);
		}
		if (close + 1 <= open) {
			f(s + ")", open, close + 1);
		}
	};
	f("", 0, 0);

	return res;
};
