/*
    1st approach:
	- start traversing the input array from the below index and i-=1, j+=1

    e.g.
    [1,2,3]
    [4,5,6]
    [7,8,9]
    
    start from:
    row idx 0, [1] 			
    row idx 1, [4,2] 		   then reverse
    row idx 2, [7,5,3] 	    
    col idx 1, [8,6] 		   then reverse
    col idx 2, [9] 			

	- put the items to the result array
	- for odd rows, put reversely
    
	Time		O(m*n)
	Space		O(m*n) the 2D array
	540 ms, faster than 16.55%
*/
var findDiagonalOrder = function (M) {
	if (M.length == 0 || M[0].length == 0) {
		return [];
	}
	const R = M.length;
	const C = M[0].length;
	const res = [];
	for (let i = 0; i < R; i++) {
		let arr = [];
		let i_ = i;
		let j = 0;
		while (i_ >= 0 && j < C) {
			arr.push(M[i_][j]);
			i_ -= 1;
			j += 1;
		}
		res.push(arr);
	}
	for (let j = 1; j < C; j++) {
		let arr = [];
		let i = R - 1;
		let j_ = j;
		while (i >= 0 && j_ < C) {
			arr.push(M[i][j_]);
			i -= 1;
			j_ += 1;
		}
		res.push(arr);
	}
	let final = [];
	for (let i = 0; i < res.length; i++) {
		const arr = res[i];
		if (i % 2 == 1) {
			final = final.concat(arr.reverse());
		} else {
			final = final.concat(arr);
		}
	}
	return final;
};
