/*
    classic approach: math recursively
    - split the n (divide and conquer)

            2^10
        (2*2=4) ^5
    (4 * 4) ^ 2 * 4 

    Time    O(logn)
    Space   O(logn) recursion tree
    56 ms, faster than 98.58%
*/
var myPow = function(x, n) {
    if (n < 0) {
        return 1 / f(x, -n)
    }
    return f(x, n)
};

const f = (x, n) => {
    if (n == 0) {
        return 1
    }
    const mid = Math.floor(n/2)
    const p = f(x, mid)
    if (n % 2 == 0) {
        return p * p
    }
    return p * p * x
}

/*
    classic approach: math recursively
    - split the n (divide and conquer)

            2^10
        (2*2=4) ^5
    (4 * 4) ^ 2 * 4 

    Time    O(logn)
    Space   O(logn) recursion tree
    92 ms, faster than 26.11%
*/
var myPow = function (x, n) {
	if (n == 0) {
		return 1;
	}

	let N = Math.abs(n);

	const mods = [];
	while (N > 1) {
		if (N % 2 == 1) {
			mods.push(x);
		}
		x = x * x;
		N = Math.floor(N / 2);
	}
	for (let m of mods) {
		x *= m;
	}

	return n > 0 ? x : 1 / x;
};
