/**
 * @param {string} s
 * @return {boolean}
 */

/*
    aabb xxy bbaa
         ^ ^
    then check if s[left:right] isPalindrome
    
    aabb yxx bbaa
         ^ ^
    then check if s[left+1:right+1] isPalindrome
    
*/
var validPalindrome = function(s) {
    let left = 0
    let right = s.length - 1
    while (left < right) {
        if (s[left] == s[right]) {
            left += 1
            right -= 1
        } else {
            const a = isPalindrome(s.slice(left, right))
            const b = isPalindrome(s.slice(left+1, right+1))
            return a || b
        }
    }
    return true
};

const isPalindrome = s => {
    let r = ''
    for (let i = s.length-1; i >= 0; i--) {
        r += s[i]
    }
    return s === r
}