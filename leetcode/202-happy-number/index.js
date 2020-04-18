/**
 *  1st approach: hashtable

    e.g.1 => 19
    
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 02 = 1
    return True

    e.g.2 => 2
    2^2 = 4
    4^2 = 16
    1^2 + 6^2 = 37
    3^2 + 7^2 = 58
    5^2 + 8^2 = 89
    8^2 + 9^2 = 145
    1^2 + 4^2 + 5^2 = 42
    4^2 + 2^2 = 20
    2^2 + 0^2 = 4 <------------ seen!!!
    return False

    Time    O(?) it is hard to determind, but any number can only appear once at most, so the upperbound is O(2^31-1)
    Space   O(?) the upperbound is O(2^31-1)
    16 ms, faster than 96.23%
    
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
	const hs = new Set();
	while (n > 1) {
		const s = n.toString(10);
		let total = 0;
		for (let c of s) {
			const x = parseInt(c);
			total += x * x;
		}
		if (hs.has(total)) {
			return false;
		}
		hs.add(total);
		n = total;
	}
	return true;
};
