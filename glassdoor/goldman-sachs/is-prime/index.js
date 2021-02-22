const isPrime = n => {
    if (n < 2) {
        return false
    }
    let i = 2
    while (i * i <= n) {
        const dividend = Math.floor(n / i)
        if (dividend * i == n) {
            return false
        }
        i += 1
    }
    return true
}

console.assert(isPrime(1) == false)
console.assert(isPrime(2) == true)
console.assert(isPrime(3) == true)
console.assert(isPrime(4) == false)
console.assert(isPrime(5) == true)
console.assert(isPrime(6) == false)
console.assert(isPrime(7) == true)
console.assert(isPrime(8) == false)
console.assert(isPrime(9) == false)
console.assert(isPrime(10) == false)
console.assert(isPrime(11) == true)
console.assert(isPrime(12) == false)
console.assert(isPrime(13) == true)
console.assert(isPrime(14) == false)
console.assert(isPrime(15) == false)
console.assert(isPrime(16) == false)
console.log("-----")
console.assert(isPrime(101) == true)
console.assert(isPrime(102) == false)
console.assert(isPrime(103) == true)
console.assert(isPrime(104) == false)
console.assert(isPrime(105) == false)
console.assert(isPrime(106) == false)
console.assert(isPrime(107) == true)
console.assert(isPrime(108) == false)
console.assert(isPrime(109) == true)