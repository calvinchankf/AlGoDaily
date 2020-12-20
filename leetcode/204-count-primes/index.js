/*
    hashtable

    ref:
    - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    Time    O(N log (log N)) <- according to the article
    Space   O(N)
    136 ms, faster than 81.25%
*/
var countPrimes = function(n) {
    const isPrime = Array(n).fill(true)
    isPrime[0] = false
    isPrime[1] = false
    let res = 0
    for (let i = 2; i < n; i++) {
        if (isPrime[i] === false) {
            continue
        }
        res += 1
        for (let j = 2; i*j < n; j++) {
            isPrime[i*j] = false
        }
    }
    return res
};