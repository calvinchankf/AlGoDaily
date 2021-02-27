/*
    1st: brute force string.startswith()

    Time    O(MN)
    Space   O(1)
    64 ms, faster than 99.06%
*/
var isPrefixOfWord = function(sentence, searchWord) {
    const words = sentence.split(' ')
    for (let i = 0; i < words.length; i++) {
        const w = words[i]
        if (w.indexOf(searchWord) == 0) {
            return i + 1
        }
    }
    return -1
};