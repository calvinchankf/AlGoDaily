/*
    https://leetcode.com/discuss/interview-question/394477/

    Given an integer, find out whether it is a power of 10 or not.
*/
let powerOfTen

// 1st: log
powerOfTen = (n) => {
    if (n < 1) { return false }
    const x = Math.floor(Math.log(n) / Math.log(10))
    return 10**x == n
}
console.log(powerOfTen(-10))
console.log(powerOfTen(-1))
console.log(powerOfTen(0))
console.log(powerOfTen(1))
console.log(powerOfTen(2))
console.log(powerOfTen(10))
console.log(powerOfTen(11))
console.log(powerOfTen(20))
console.log(powerOfTen(22))
console.log(powerOfTen(100))

console.log("-----")

// 2nd: division
powerOfTen = (n) => {
    if (n < 1) { return false }
    while (n > 1) {
        if (n%10 != 0) { return false}
        n /= 10
    }
    return true
}
console.log(powerOfTen(-10))
console.log(powerOfTen(-1))
console.log(powerOfTen(0))
console.log(powerOfTen(1))
console.log(powerOfTen(2))
console.log(powerOfTen(10))
console.log(powerOfTen(11))
console.log(powerOfTen(20))
console.log(powerOfTen(22))
console.log(powerOfTen(100))

console.log("-----")

// 3rd: check zeros
powerOfTen = (n) => {
    let startFromOne = false
    if (n < 1) { return false }
    const s = `${n}`
    for (let c of s) {
        if (c == '1') {
            if (startFromOne == true) { return false }
            startFromOne = true
        } else if (c != '0') {
            return false
        }
    }
    return true
}

console.log(powerOfTen(-10))
console.log(powerOfTen(-1))
console.log(powerOfTen(0))
console.log(powerOfTen(1))
console.log(powerOfTen(2))
console.log(powerOfTen(10))
console.log(powerOfTen(11))
console.log(powerOfTen(20))
console.log(powerOfTen(22))
console.log(powerOfTen(100))