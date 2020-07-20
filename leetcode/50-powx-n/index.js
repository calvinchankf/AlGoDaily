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
const myPow = (x, n) => {
	const N = Math.abs(n);
	if (n >= 0) {
		return f(x, N);
	}
	return 1 / f(x, N);
};

const f = (x, n) => {
	if (n === 0) {
		return 1;
	}
	const half = f(x, Math.floor(n / 2));
	if (n % 2 == 0) {
		return half * half;
	}
	return half * half * x;
};

/*
    classic approach 2: math recursively
    - split the n (divide and conquer)

            2^10
        (2*2=4) ^5
    (4 * 4) ^ 2 * 4 

    Time    O(logn)
    Space   O(logn) recursion tree
    104 ms, faster than 17.12% 
*/
var myPow = function (x, n) {
	if (n === 0) {
		return 1;
	}

	if (n === 1) {
		return x;
	} else if (n === -1) {
		return 1 / x;
	}

	if (n % 2 === 0) {
		return myPow(x * x, Math.floor(n / 2));
	} else {
		return myPow(x * x, Math.floor(n / 2)) * x;
	}
};

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
