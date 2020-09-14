/*
    1st: sort + queue
    - first sort the input in a reversed order
    - then put the each person into a correct position

    e.g. [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    sort the input: [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    
    1st iteration: [7, 0]
    remaining: [[7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    
    2nd iteration: [[7, 0], [7, 1]]
    remaining: [[6, 1], [5, 0], [5, 2], [4, 4]]
    
    3rd iteration: [[7, 0], [6, 1], [7, 1]]
    remaining: [[5, 0], [5, 2], [4, 4]]
    
    4th iteration: [[5, 0], [7, 0], [6, 1], [7, 1]]
    remaining: [[4, 4], [5, 2]]

    5th iteration: [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
    remaining: [[4, 4]]

    final iteration: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
*/
var reconstructQueue = function (people) {
	const nums = [...people].sort((a, b) => {
		if (a[0] == b[0]) {
			return a[1] - b[1];
		}
		return b[0] - a[0];
	});
	const res = [];
	while (nums.length > 0) {
		const [h, k] = nums.shift();
		if (k == 0) {
			res.splice(0, 0, [h, k]);
		}
		let count = 0;
		for (let i = 0; i < res.length; i++) {
			if (res[i][0] >= h) {
				count += 1;
			}
			if (count == k) {
				res.splice(i + 1, 0, [h, k]);
				break;
			}
		}
	}
	return res;
};
