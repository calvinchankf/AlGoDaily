/*
    1st approach: learned from others
    - the basic idea is to find the common prefix of m and n

    e.g.1
    m, n = 11, 15
    num,bit representation
    11  1011
    12  1100
    13  1101
    14  1110
    15  1111

    the common prefix is 1000 -> 8

    e.g.2
    m, n = 10, 11
    num,bit representation
    10  1010
    11  1011

    the common prefix is 1010 -> 10

    ref:
    - http://www.cnblogs.com/grandyang/p/4431646.html

    Time    O(k) k: max number of bits of m and n
    Space   O(1)
    36 ms, faster than 99.61%
*/

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var rangeBitwiseAnd = function (m, n) {
	let i = 0;
	while (m != n) {
		m >>= 1;
		n >>= 1;
		i += 1;
	}
	return m << i;
};
