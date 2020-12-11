/*
    1st approach: sort
	1. count num: freq into a hashtable
	2. sort the hashtable keys by frequency
	3. append the key to the result according to a descending index order(freqency)

	Time	O(n)
	Space	O(n)
	100 ms, faster than 58.74%
*/
var frequencySort = function (s) {
	const ht = {};
	for (let c of s) {
		if (c in ht) {
			ht[c] += 1;
		} else {
			ht[c] = 1;
		}
	}
	const freqs = [];
	for (let k in ht) {
		freqs.push([ht[k], k]);
	}
	freqs.sort((a, b) => {
		if (a[0] == b[0]) {
			return b[1] - a[1] ? -1 : 1;
		}
		return b[0] - a[0];
	});

	let res = "";
	for (let [f, c] of freqs) {
		res += c.repeat(f);
	}
	return res;
};

/*
    2nd approach: bucket sort
	1. count num: freq into a hashtable
	2. sort the hashtable keys by frequency
	3. append the key to the result according to a descending index order(freqency)

	Time	O(n)
	Space	O(n)
	132 ms, faster than 12.65%
*/
var frequencySort = function(s) {
    const ht = {}
    for (let c of s) {
        if (c in ht) {
            ht[c] += 1
        } else {
            ht[c] = 1
        }
    }
    const freqs = []
    for (let k in ht) {
        freqs.push([ht[k], k])
    }
    freqs.sort((a, b) => {
        if (a[0] == b[0]) {
            return b[1] - a[1] ? -1 : 1
        }
        return b[0] - a[0]
    })
    
    let res = ''
    for (let [f, c] of freqs) {
        res += c.repeat(f)
    }
    return res
};
