var reverseWords = function(s) {
    s = s.trim()
    const words = s.split(' ')
    let res = ''
    const n = words.length
    for (let i = n-1; i >= 0; i--) {
        if (words[i].length > 0) {
            res += words[i] + ' '
        }
    }
    return res.slice(0, res.length-1)
};