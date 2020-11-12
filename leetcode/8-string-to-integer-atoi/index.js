/*
    1st approach
	- straight forward but annoying approach
	- be careful of the corner cases

	Time 	O(n) n=length of input string
	Space O(1)
	100 ms, faster than 67.89%
*/
var myAtoi = function(s) {
    s = s.trim()
    if (s.length == 0) {
        return 0
    }

    let num = 0
    let sign = 0
    if (s[0] == '+') {
        sign = 1
    } else if (s[0] == '-') {
        sign = -1
    } else if (isDigit(s[0])) {
        num = parseInt(s[0])
    } else {
        return 0
    }

    for (let i = 1; i < s.length; i++) {
        const c = s[i]
        if (isDigit(c)) {
            num = num*10 + parseInt(c)
        } else {
            break
        }
    }
    if (sign == 0) {
        sign = 1
    }
    const res = sign * num
    
    if (res < -(2**31)) {
        return -(2**31)
    } else if (res > 2**31 - 1) {
        return 2**31-1
    }
    return res
};

const isDigit = (c) => {
    return '0123456789'.indexOf(c) > -1
}

console.log(myAtoi('42'))
console.log(myAtoi('-42'))
console.log(myAtoi(' -42'))
console.log(myAtoi('4193 with words'))
console.log(myAtoi('words and 987'))
console.log(myAtoi('22 and 987'))
console.log(myAtoi(' -22 and 987'))
console.log(myAtoi(' -+22 and 987'))
console.log(myAtoi('-91283472332'))
console.log(myAtoi('-91283472332 a'))
console.log(myAtoi(' -91283472332'))
console.log(myAtoi(' -91283472332 a'))
console.log(myAtoi(' a-91283472332'))
console.log(myAtoi('00000-42a1234'))
