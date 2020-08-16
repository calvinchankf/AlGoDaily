/*
    1st: top-down recursive
	- use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	    n for hashtable, n for recursive callstack
	68 ms, faster than 79.80% 
*/
var fib = function (N) {
	const ht = {};
	const f = (n) => {
		if (n == 0) {
			return 0;
		} else if (n == 1) {
			return 1;
		}
		if (n in ht) {
			return ht[n];
		}
		const temp = f(n - 1) + f(n - 2);
		ht[n] = temp;
		return temp;
	};
	return f(N);
};
