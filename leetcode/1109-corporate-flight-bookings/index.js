/*
    1st: math
    - similar to lcl094, 1589
    - typical range frequency counting technique to deal with values on a range
    - basically we can just use the prefix-sum concept to mark the start and the end of each interval
    - ./idea.jpeg

    Time    O(2n)
    Space   O(n)
    180 ms, faster than 86.44%
*/
var corpFlightBookings = function (bookings, n) {
	const res = Array(n + 2).fill(0);
	for (let [i, j, k] of bookings) {
		res[i] += k;
		res[j + 1] -= k;
	}
	for (let i = 1; i < n + 1; i++) {
		res[i] += res[i - 1];
	}
	return res.slice(1, res.length - 1);
};
