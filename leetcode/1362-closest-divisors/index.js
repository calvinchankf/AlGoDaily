/*
    1st: factorization
    - get the factors of num+1 and num+2
    - compare and return the result

    Time    O(2 * sqrt(N))
    Space   O(4)
    136 ms, faster than 12.00% 
*/
var closestDivisors = function (num) {
	const [a1, b1] = factorization(num + 1);
	const [a2, b2] = factorization(num + 2);
	if (Math.abs(a1 - b1) < Math.abs(a2 - b2)) {
		return [a1, b1];
	}
	return [a2, b2];
};

const factorization = (n) => {
	const root = Math.ceil(Math.sqrt(n));
	const res = new Set();
	for (let i = root; i > 0; i--) {
		if (n % i == 0) {
			return [i, n / i];
		}
	}
};
