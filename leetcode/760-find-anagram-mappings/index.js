/*
    1st: hashtable

	Time		O(N)
	Space		O(N)
	80 ms, faster than 48.43%
*/
var anagramMappings = function(A, B) {
    const ht = {}
    for (let i = 0; i < B.length; i++) {
        const b = B[i]
        if (b in ht) {
            ht[b].push(i)
        } else {
            ht[b] = [i]
        }
    }
    const res = []
    for (let i = 0; i < A.length; i++) {
        const a = A[i]
        if (a in ht) {
            res.push(ht[a].pop())
        }
    }
    return res
};