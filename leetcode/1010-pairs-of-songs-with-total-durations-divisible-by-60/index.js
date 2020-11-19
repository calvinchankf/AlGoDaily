/*
    math

    1st approach: math + hashtable
    - we only need to consider each song length modulo 60
    - we can count the number of songs with (length % 60) equal to r, and store that in an array of size 60

    e.g. [60, 60, 20, 40, 100, 63]
    cache[0] = 2
    cache[3] = 1
    cache[20] = 1
    cache[40] = 2

    cache[0] can pair with cache[0]
    cache[20] can pair with cache[40]
    ....etc

    Time    O(n)
    Space   O(n)
    92 ms, faster than 66.97%
*/
var numPairsDivisibleBy60 = function(time) {
    const cache = Array(60).fill(0)
    let res = 0
    for (let t of time) {
        const r = t%60
        const remain = (60 - r)%60
        if (cache[remain] > 0) {
            res += cache[remain]
        }
        cache[r] += 1
    }
    return res
};