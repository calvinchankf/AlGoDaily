/*
    1st approach: hashtable + sort

    Time    O(L + WLogN)
    Space   O(K)
    76 ms, faster than 55.30%
*/
var shortestCompletingWord = function (licensePlate, words) {
	licensePlate = licensePlate.toLowerCase();
	const ht = {};
	for (let c of licensePlate) {
		if ("abcdefghijklmnopqrstuvwxyz".indexOf(c) > -1) {
			if (c in ht) {
				ht[c] += 1;
			} else {
				ht[c] = 1;
			}
		}
	}
	words.sort((a, b) => a.length - b.length);
	for (let w of words) {
		const temp = {};
		for (let c of w) {
			if (c in temp) {
				temp[c] += 1;
			} else {
				temp[c] = 1;
			}
		}
		let ifContain = true;
		for (let key in ht) {
			if (temp[key] === undefined || ht[key] > temp[key]) {
				ifContain = false;
				break;
			}
		}
		if (ifContain) {
			return w;
		}
	}
	return "";
};

/*
    2nd approach: hashtable

    Time    O(L+W)
    Space   O(K)
    76 ms, faster than 55.30%
*/
var shortestCompletingWord = function (licensePlate, words) {
	licensePlate = licensePlate.toLowerCase();
	const ht = {};
	for (let c of licensePlate) {
		if ("abcdefghijklmnopqrstuvwxyz".indexOf(c) > -1) {
			if (c in ht) {
				ht[c] += 1;
			} else {
				ht[c] = 1;
			}
		}
	}

	let res = "aaaaaaaaaaaaaa";
	for (let w of words) {
		const temp = {};
		for (let c of w) {
			if (c in temp) {
				temp[c] += 1;
			} else {
				temp[c] = 1;
			}
		}
		let ifContain = true;
		for (let key in ht) {
			if (temp[key] === undefined || ht[key] > temp[key]) {
				ifContain = false;
				break;
			}
		}
		if (ifContain && w.length < res.length) {
			res = w;
		}
	}
	return res;
};
