/*
    1st: hashtable

    Time    O(NR)
    Space   O(N)
    144 ms, faster than 100.00%
*/
var mostVisited = function (n, rounds) {
	let start = rounds[0];
	let cur = start;
	for (let i = 1; i < rounds.length; i++) {
		const p = rounds[i - 1];
		const c = rounds[i];
		if (c <= p) {
			const diff = c + n - p;
			cur += diff;
		} else {
			cur += c - p;
		}
	}

	const freqs = {};
	for (let i = 1; i <= n; i++) {
		freqs[i] = 0;
	}

	for (let i = start; i <= cur; i++) {
		if (i % n == 0) {
			freqs[n] += 1;
		} else {
			freqs[i % n] += 1;
		}
	}
	// console.log(freqs);

	let res = [];
	let maxFreq = 0;
	for (let key in freqs) {
		if (res.length == 0) {
			res.push(key);
			maxFreq = freqs[key];
			continue;
		}
		if (freqs[key] > maxFreq) {
			maxFreq = freqs[key];
			res = [key];
		} else if (freqs[key] == maxFreq) {
			res.push(key);
		}
	}
	return res;
};

/*
    2nd: we just care about the start and the end

    There are 2 cases:
    1. If start <= end, return the range [start, end].
    2. If end < start, return the range [1, end] + range [start, n].

    Time    O(N)
    Space   O(N)
    92 ms, faster than 100.00%
*/
var mostVisited = function (n, rounds) {
	let start = rounds[0];
	let end = rounds[rounds.length - 1];
	if (start < end) {
		const res = [];
		for (let i = start; i <= end; i++) {
			res.push(i);
		}
		return res;
	} else if (start == end) {
		return [start];
	}
	const res = [];
	for (let i = 1; i <= end; i++) {
		res.push(i);
	}
	for (let i = start; i <= n; i++) {
		res.push(i);
	}
	return res;
};
