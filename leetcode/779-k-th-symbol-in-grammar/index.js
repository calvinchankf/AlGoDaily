/*
    1st approach: better brute force
	Time	O(2^n)
	Space	O(1)
	TLE
*/
var kthGrammar = function(N, K) {
    let cur = '0'
    for (let i = 0; i < N; i++) {
        let temp = ''
        for (let j = 0; j < cur.length; j++) {
            if (cur[j] == '0') {
                temp += '01'
            } else {
                temp += '10'
            }   
        }
        cur = temp
        // console.log(cur)
    }
    return cur[K-1]
};

