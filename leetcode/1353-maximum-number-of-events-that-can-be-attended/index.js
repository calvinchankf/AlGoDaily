/*
    1st: sort + brute force
    
    Time    O(N*K) K = average length of an interval
    Space   O(10^5)
    TLE 44 / 45 test cases passed. 
*/
var maxEvents = function (events) {
	events.sort((a, b) => {
		if (a[1] == b[1]) {
			return a[0] - b[0];
		}
		return a[1] - b[1];
	});

	let res = 0;
	const days = Array(10 ** 5 + 1).fill(false);
	for (let i = 0; i < events.length; i++) {
		const [s, e] = events[i];
		for (let j = s; j <= e; j++) {
			if (days[j] == false) {
				days[j] = true;
				res += 1;
				break;
			}
		}
	}
	return res;
};
