/*
    similar to lc44, 712, 583

    questions to ask:
    - are the cost of add, delete, remove the same? yes
    - will there be empty strings? yes

    classic dynamic programming approach
    - https://www.youtube.com/watch?v=We3YDTzNXEk

    dp meaning:

    edit    |   insert
    -------------------
    delete  |   newstring

    insert means: insert one chracter to the horizontal string to form the vertical string
    delete means: delete one chracter from the horizontal string to form the vertical string
    edit means  : edit one chracter on the horizontal string to form the vertical string

    Time    O(word1 * word2)
    Space    O((word1+1) * (word2+1))
    196 ms, faster than 22.57%
*/
var minDistance = function (str1, str2) {
	const dp = [];
	const l1 = str1.length;
	const l2 = str2.length;
	for (let i = 0; i < l1 + 1; i++) {
		const temp = [];
		for (let j = 0; j < l2 + 1; j++) {
			if (i == 0) {
				temp.push(j);
			} else if (j == 0) {
				temp.push(i);
			} else {
				temp.push(0);
			}
		}
		dp.push(temp);
	}
	for (let i = 0; i < l1; i++) {
		for (let j = 0; j < l2; j++) {
			if (str1[i] == str2[j]) {
				dp[i + 1][j + 1] = dp[i][j];
			} else {
				dp[i + 1][j + 1] =
					Math.min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1;
			}
		}
	}
	console.log(dp);
	return dp[l1][l2];
};
