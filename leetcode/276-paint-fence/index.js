/*
    1st: math, dynamic programming
    
    day[1] = k
    day[2] = k * k
    day[i>2] = (day[i-1] + day[i-2]) * (k - 1)

    on day i, there are 2 cases

    case 1:
    dont form duplicate combination with the previous day, day[i-1] * (k-1)

    case 2:
    form duplicate combination with the day before previous day, day[i-2] * (k-1)

    ref:
    - https://leetcode.com/problems/paint-fence/discuss/71151/Lucas-formula-maybe-%22O(1)%22-and-34-liners
    - https://www.dazhuanlan.com/2020/01/04/5e10205cdf382/

    Time    O(N)
    Space   O(N)
    76 ms, faster than 63.29%
*/
var numWays = function (n, k) {
	return f(n, k, {});
};

const f = (n, k, ht) => {
	if (n == 0) {
		return 0;
	}
	if (n == 1) {
		return k;
	}
	if (n == 2) {
		return k * k;
	}
	if (n in ht) {
		return ht[n];
	}
	const ways = (f(n - 2, k, ht) + f(n - 1, k, ht)) * (k - 1);
	ht[n] = ways;
	return ht[n];
};
