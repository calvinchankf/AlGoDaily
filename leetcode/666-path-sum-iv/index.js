/*
    2nd: math + hashtable
    1. create an 2D array which store the nodes with each of the corresponding position
    2. find the leaves, by using 2*p and 2*p + 1
    3. from each leave, traverse upward and add up the node values along the path

    Time    O(N)
    Space   O(N)
    80 ms, faster than 85.71%
*/
var pathSum = function (nums) {
	if (nums.length == 0) {
		return 0;
	}
	// 1)
	const ht = [];
	for (let i = 0; i < 5; i++) {
		ht.push(Array(16).fill(-1));
	}
	for (let num of nums) {
		const s = num.toString();
		const d = parseInt(s[0]) - 1;
		const p = parseInt(s[1]) - 1;
		const v = parseInt(s[2]);
		ht[d][p] = v;
	}

	// 2)
	const leaves = [];
	for (let i = 0; i < 4; i++) {
		for (let j = 0; j < 8; j++) {
			if (ht[i][j] > -1) {
				const left = ht[i + 1][j * 2];
				const right = ht[i + 1][j * 2 + 1];
				if (left == -1 && right == -1) {
					leaves.push(`${i + 1}${j + 1}${ht[i][j]}`);
				}
			}
		}
	}

	// 3)
	let res = 0;
	for (let leave of leaves) {
		const s = leave.toString();
		let d = parseInt(s[0]) - 1;
		let p = parseInt(s[1]) - 1;
		let temp = 0;
		while (d >= 0) {
			temp += ht[d][p];
			d -= 1;
			p = Math.floor(p / 2);
		}
		res += temp;
	}
	return res;
};
