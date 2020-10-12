/*
    1st approach: similar to zero sum subarray
    - if prefixSum[i]%K == prefixSum[j]%k, it means that A[i+1:j] is divisible by K

    ref:
    - https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217979/Pictured-Explanation-Python-O(n)-Clean-Solution-8-Lines!

    Time    O(n)
    Space   O(n)
    268 ms, faster than 94.01%
*/
var subarraysDivByK = function (A, K) {
	let res = 0;
	const ht = {};
	let pfs = 0;
	for (let i = 0; i < A.length; i++) {
		pfs += A[i];
		if (pfs % K == 0) {
			res += 1;
		}

		// -10%7 = -3, but what I want is -10%7 = 4
		let mod = pfs % K;
		if (mod < 0) {
			mod += K;
		}

		// prefixSum[i]%K == prefixSum[j]%k, it means that A[i+1:j] is divisible by K
		if (mod in ht) {
			res += ht[mod];
		}
		// put it in hashtable
		if (mod in ht) {
			ht[mod] += 1;
		} else {
			ht[mod] = 1;
		}
	}
	return res;
};
