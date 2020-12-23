/*
    1st approach: stack

    Time    O(2N)
    Space   O(N)
    176 ms, faster than 39.59%
*/
var romanToInt = function(s) {
    const ht = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    const stack = [];
    const n = s.length
    for (let x of s) {
        const num = ht[x]
        if (num > stack[stack.length-1]) {
            const prev = stack.pop()
            stack.push(num - prev)
        } else {
            stack.push(num)
        }
    }
    return stack.reduce((total, cur) => total + cur, 0)
};

/*
    1st: array + hashtable
    - assume the input is legit all the time, then we dont need to care about e.g. MID

    Time    O(N)
    Space   O(1)
    152 ms, faster than 87.83% 
*/
var romanToInt = function (s) {
	const ht = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    let res = 0
    const n = s.length
    for (let i = 0; i < s.length; i++) {
        const num = ht[s[i]]
        if (i > 0 && num > ht[s[i-1]]) {
            res -= ht[s[i-1]]
            res += num - ht[s[i-1]]
        } else {
            res += num
        }
    }
    return res
};