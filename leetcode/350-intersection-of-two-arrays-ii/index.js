/*
    1st approach: hashtable

    Time    O(M+N)
    Space   O(M)
    80 ms, faster than 77.14%
*/
var intersect = function (nums1, nums2) {
	const ht = {};
	for (let x of nums1) {
		if (x in ht) {
            ht[x] += 1
        } else {
            ht[x] = 1
        }
	}
    const res = []
	for (let x of nums2) {
        if (x in ht && ht[x] > 0) {
            res.push(x)
            ht[x] -= 1
        }
    }
    return res
};

/*
    2nd approach: 2 hashtables

    Time    O(M+N+MN)
    Space   O(M)
    88 ms, faster than 34.93%
*/
var intersect = function(nums1, nums2) {
    const ht1 = {};
	for (let x of nums1) {
		if (x in ht1) {
            ht1[x] += 1
        } else {
            ht1[x] = 1
        }
	}
	const ht2 = {};
	for (let x of nums2) {
		if (x in ht2) {
            ht2[x] += 1
        } else {
            ht2[x] = 1
        }
	}
    const res = []
    for (let key in ht1) {
        if (key in ht2) {
            const c = Math.min(ht1[key], ht2[key])
            const sub = Array(c).fill(key)
            res.push(...sub)
        }
    }
    return res
};
