/*
    https://www.1point3acres.com/bbs/thread-690568-1-1.html
*/
const getPrimeFactors = n => {
    const factors = new Set()
    let i = 2
    while (i * i <= n) {
        if (n % i == 0) {
            factors.add(i)
            n = Math.floor(n / i)
        } else {
            i += 1
        }
    }
    if (n > 1) { factors.add(n) }
    return Array.from(factors)
}

console.log(getPrimeFactors(40))
console.log(getPrimeFactors(60))
console.log(getPrimeFactors(400))
console.log(getPrimeFactors(500))
console.log(getPrimeFactors(2310))