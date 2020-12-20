/*
    1st approach: sort

    Time    O(n)
    Space   O(n)
    16 ms, faster than 95.04%
*/
var heightChecker = function (heights) {
	const n = heights.length
    const clone = [...heights]
    clone.sort((a, b) => a - b)
    let res = 0
    for (let i = 0; i < n; i++) {
        if (heights[i] != clone[i]) {
            res += 1
        }
    }
    return res
};
