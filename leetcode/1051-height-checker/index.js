/*
    1st approach: sort

    Time    O(n)
    Space   O(n)
    16 ms, faster than 95.04%
*/
var heightChecker = function (heights) {
	const clone = [...heights]
    clone.sort((a, b) => a - b)
    let count = 0
    for (let i = 0; i < clone.length; i++) {
        if (clone[i] != heights[i]) {
            count += 1
        }
    }
    return count
};
