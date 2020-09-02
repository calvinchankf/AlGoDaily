/*
    classic approach:
    - bottom up dynamic programming 
    - select the path with min cost from bottom to top, mutate the input array
    Time	O(n)
    Space	O(1)
    24 ms, faster than 91.10%
*/
var minimumTotal = function (triangle) {
	const n = triangle.length;
	for (let i = n - 2; i >= 0; i--) {
		for (let j = 0; j < triangle[i].length; j++) {
			triangle[i][j] += Math.min(
				triangle[i + 1][j],
				triangle[i + 1][j + 1]
			);
		}
	}
	return triangle[0][0];
};
