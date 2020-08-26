/*
    1st approach: stack + carry
	- each digit = byteA + byteB + carry
	- add the digits until no more carry, a, b

    Time    O(A+B + max(A, B))
    Space   O(A+B)
    92 ms, faster than 33.74%
*/
var addBinary = function (a, b) {
	let carry = 0;
	let res = "";
	while (a.length > 0 || b.length > 0) {
		let x = 0;
		if (a.length > 0) {
			x = parseInt(a[a.length - 1]);
			a = a.slice(0, -1);
		}

		let y = 0;
		if (b.length > 0) {
			y = parseInt(b[b.length - 1]);
			b = b.slice(0, -1);
		}
		const z = (x + y + carry) % 2;
		carry = Math.floor((x + y + carry) / 2);
		res = String(z) + res;
	}
	if (carry > 0) {
		res = "1" + res;
	}
	return res;
};
